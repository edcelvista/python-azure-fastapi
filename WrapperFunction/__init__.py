import azure.functions as func
import fastapi
from WrapperFunction.db_check import check_database  # Import the function from db_check.py

app = fastapi.FastAPI()

@app.get("/checkDB")
async def index():
    # Invoke the check_database function
    result = await check_database()
    return {
        "results": str(result),
    }

@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }
