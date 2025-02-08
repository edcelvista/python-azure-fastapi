import azure.functions as func
import fastapi
from fastapi.middleware.wsgi import WSGIMiddleware
from WrapperFunction.db_check import check_database  # Import the function from db_check.py

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Azure Functions!"}

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Use Uvicorn to run FastAPI app
    if req.method == "GET":
        return func.HttpResponse(
            content=JSONResponse(app(req)).body,
            status_code=200,
            mimetype="application/json"
        )
    else:
        return func.HttpResponse(
            "Method Not Allowed", status_code=405
        )

@app.get("/checkDB")
async def databasecheck():
    # Invoke the check_database function
    result = await check_database()
    return {
        "results": str(result),
    }

