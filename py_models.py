from pydantic import BaseModel

class Code_Request(BaseModel):
    code: str
    lang_id: str 
    stdin: str | None= None

class Execution_Out(BaseModel):
    stdout: str | None= None
    stderr: str | None= None