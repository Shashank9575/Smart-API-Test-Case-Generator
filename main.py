from fastapi import FastAPI
from pydantic import BaseModel
from src.gen_test_cases import TestCaseGenerator

class GitRepo(BaseModel):
    repo_name: str

# Use raw string or double backslashes
GenTestCases = TestCaseGenerator(
    configuration_file_path=r"D:\Doccument\project\Testing\ai-code-tester\sample_config.json"
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ai-driven test case generator"}

@app.post("/generate-test-cases")
async def generate_test_cases(repository: GitRepo):
    repo_name = repository.repo_name
    resp = GenTestCases.get_test_cases(repo_name=repo_name)
    return {"message": resp"}

# 👇 Add this block to make `python main.py` work
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
