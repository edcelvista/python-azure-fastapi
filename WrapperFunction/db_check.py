import os
import asyncpg
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
