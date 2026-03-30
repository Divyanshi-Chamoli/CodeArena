from fastapi import FastAPI
import asyncio, httpx
from fastapi.responses import HTMLResponse, JSONResponse
from dotenv import load_dotenv
load_dotenv()
from config import *
from py_models import *
from encode import *
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def dashboard():
    with open("static/dashboard.html", encoding="utf-8") as f:
        return f.read()

@app.get("/problems")
def get_problems():
    return [{"id": p["id"], "title": p["title"], "difficulty": p["difficulty"], "tags": p["tags"]} for p in PROBLEMS]

@app.get("/problems/{problem_id}")
def get_problem(problem_id: int):
    problem = next((p for p in PROBLEMS if p["id"] == problem_id), None)
    if not problem:
        return JSONResponse(status_code=404, content={"detail": "Not found"})
    return problem

@app.post("/run")
async def run_code(src_code: Code_Request):
    payload = {
        "language_id": LANGUAGE_IDS[src_code.lang_id.lower()], #use the lowercse func to reduce error+if not in dict, handle error
        "source_code": encode_base64(src_code.code),
        "stdin": encode_base64(src_code.stdin)
    }

    async with httpx.AsyncClient() as client:
        response= await client.post(RAPIDAPI_URL,
        headers=headers,
        params={"base64_encoded": "true", "wait": "false", "fields":"*"},
        json= payload)

        token= response.json().get("token")
        # Poll until done
        for _ in range(10):
            await asyncio.sleep(1.5)
            result_resp = await client.get(
                f"{RAPIDAPI_URL}/{token}",
                headers=headers,
                params={"base64_encoded": "true", "fields": "*"}
            )
            result = result_resp.json()
            if result.get("status", {}).get("id") not in (1, 2):
                break

    stdout = decode_base64(result.get("stdout"))
    stderr = decode_base64(result.get("stderr"))
    compile_output = decode_base64(result.get("compile_output"))
    status = result.get("status", {}).get("description", "Unknown")

    return {
        "verdict": status,
        "stdout": stdout,
        "stderr": stderr,
        "compile_output": compile_output,
        "execution_time": f"{result.get('time')}s" if result.get("time") else None,
        "memory": f"{result.get('memory')} KB" if result.get("memory") else None,
    }

@app.post("/submit/{problem_id}")
async def submit_code(problem_id: int, src_code: Code_Request):
    problem = next((p for p in PROBLEMS if p["id"] == problem_id), None)
    if not problem:
        return JSONResponse(status_code=404, content={"detail": "Problem not found"})

    test_results = []
    passed = 0

    for i, tc in enumerate(problem["test_cases"]):
        result = await run_code(Code_Request(
            code=src_code.code,
            lang_id=src_code.lang_id,
            stdin=tc["input"]
        ))
        actual = (result["stdout"] or "").strip()
        expected = tc["expected"].strip()
        ok = actual == expected

        if ok:
            passed += 1

        test_results.append({
            "case": i + 1,
            "passed": ok,
            "input": tc["input"],
            "expected": expected,
            "actual": actual,
            "stderr": result.get("stderr"),
            "compile_output": result.get("compile_output"),
            "execution_time": result.get("execution_time"),
        })

    overall = "Accepted" if passed == len(problem["test_cases"]) else "Wrong Answer"
    return {
        "overall_verdict": overall,
        "passed": passed,
        "total": len(problem["test_cases"]),
        "test_results": test_results
    }
