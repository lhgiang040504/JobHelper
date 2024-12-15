from fastapi import FastAPI
from dotenv import dotenv_values
from fastapi.middleware.cors import CORSMiddleware
from source.configs.db_connection import MongoDB
from source.routes.CandidateManagement import router as candidate_route
from source.routes.JobManagement import router as job_route
from source.routes.JobResumeMatching import router as job_resume_matching_route

config = dotenv_values(".env")

app = FastAPI()

# Thêm CORS middleware
origins = [
    "http://localhost:3000",  # Thêm địa chỉ của frontend của bạn
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # Cho phép nguồn gốc
    allow_credentials=True,        # Cho phép gửi cookie hoặc token
    allow_methods=["*"],           # Cho phép tất cả các phương thức HTTP
    allow_headers=["*"],           # Cho phép tất cả các header
)


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
app.include_router(job_resume_matching_route, prefix="/jobresumematching", tags=["jobresumematching"])