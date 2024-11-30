from fastapi import FastAPI
from dotenv import dotenv_values
from source.configs.db_connection import MongoDB
from source.routes.CandidateManagement import router as candidate_route
from source.routes.JobManagement import router as job_route

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb = MongoDB(uri=config['MONGODB_URI'], db_name=config['MONGODB_DB'])
    await app.mongodb.init()  # Initialize the MongoDB connection
    print("Connected to MongoDB database!")

@app.on_event("shutdown")
async def shutdown_db_client():
    await app.mongodb.close()  # Close the MongoDB connection
    print("Disconnected from MongoDB database!")

app.include_router(candidate_route, prefix="/candidates", tags=["candidates"])
app.include_router(job_route, prefix="/jobs", tags=["jobs"])