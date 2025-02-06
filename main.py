import os
import asyncpg
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Database connection string
DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/health")
async def check_database():
    """Check PostgreSQL database connection."""
    try:
        # Establish a temporary connection
        conn = await asyncpg.connect(DATABASE_URL)
        await conn.close()
        return {"status": "success", "message": "Database connection successful"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Run locally
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

