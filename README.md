# CodeArena
CodeArena is a full-stack online code evaluation platform that allows users to write, run, and test code solutions to programming problems directly in the browser. It replicates the core functionality of competitive programming judges such as LeetCode, providing real-time code execution, multi-language support, and automated test case evaluation. Code execution is handled securely by [Judge0 CE](https://judge0.com/) via RapidAPI.

---
## Features

- **Multi-language support** — Python 3, JavaScript, Java, C++, and C
- **Live code editor** — CodeMirror 5 with syntax highlighting, line numbers, and language-aware modes
- **Run** — executes your code against the first test case and shows stdout, stderr, and compile output
- **Submit** — runs your code against all test cases and returns a per-case verdict
- **Clean UI** — three-panel layout: problem list, problem description, and editor with output panel

---
## Project Structure
```
.
├── main.py           # FastAPI app — routes, problem data, /run and /submit logic
├── config.py         # LANGUAGE_IDS, RapidAPI URL, and HTTP headers
├── encode.py         # Base64 encode/decode helpers
├── py_models.py      # Pydantic models (Code_Request, Execution_Out)
├── .env              # RapidAPI key (never commit this)
├── requirements.txt  # Python dependencies
└── static/
    └── index.html    # Single-file frontend
```

---

## Prerequisites

- Python 3.10+
- A [RapidAPI](https://rapidapi.com/) account with access to the **Judge0 CE** API

---

## Setup

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd codearena
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create your `.env` file**
```bash
# .env
RAPIDAPI_KEY=your_rapidapi_key_here
```

> Get your key from [RapidAPI — Judge0 CE](https://rapidapi.com/judge0-official/api/judge0-ce)

**5. Run the server**
```bash
uvicorn main:app --reload --port 8000
```

**6. Open in your browser**
```
http://localhost:8000
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Serves the frontend |
| GET | `/problems` | Lists all problems |
| GET | `/problems/{id}` | Returns full problem details |
| POST | `/run` | Executes code and returns output |
| POST | `/submit/{id}` | Evaluates code against all test cases |

Interactive API docs are available at `http://localhost:8000/docs`.

---

## Changing the RapidAPI Key

Update the value in your `.env` file and restart the server:
```
RAPIDAPI_KEY=your_new_key_here
```

---

## Adding Problems

Problems are defined as dictionaries in `main.py` inside the `PROBLEMS` list. Each entry requires:

```python
{
    "id": 3,
    "title": "Problem Title",
    "difficulty": "Easy",           # Easy | Medium | Hard
    "tags": ["Array", "Hash Table"],
    "description": "Markdown description...",
    "starter_code": {
        "python": "import sys\n# read from stdin\n",
        "javascript": "const lines = ...",
        "java": "import java.util.*;\npublic class Main { ... }",
        "cpp": "#include <iostream>\n...",
        "c": "#include <stdio.h>\n...",
    },
    "test_cases": [
        {"input": "...", "expected": "..."},
    ]
}
```

> **Important:** starter code must read inputs from `stdin`, not hardcode them, so the backend can inject test case inputs during evaluation.

---

## Requirements

```
fastapi
uvicorn
httpx
python-dotenv
pydantic
```

---
