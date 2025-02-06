import os
import asyncpg
import azure.functions as func
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

async def check_database():
    """Check database connection."""
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        await conn.close()
        return {"status": "success", "message": "Database connection successful"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

async def main(req: func.HttpRequest) -> func.HttpResponse:
    result = await check_database()
    return func.HttpResponse(str(result), mimetype="application/json")

