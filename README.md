# CV Information Extraction

This project extracts structured information from CVs using FastAPI and LangChain.

## Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)

## Setup

1. **Clone the repository**:
    ```git clone <repository-url>
    cd <repository-directory>```

2. **Create and activate a virtual environment**:
    ```python -m venv venv
    source venv/bin/activate```

3. **Install dependencies**:
    ```pip install -r requirements.txt```

4. **Set up environment variables**:
    - Copy `.env.example` to `.env`:
    ```cp .env.example .env```
    - Edit `.env` to include your `LLAMA_3_API_KEY`, `MONGODB_URI`, and `MONGODB_DB`.

## Running the Application

1. **Start the FastAPI server**:
    ```uvicorn main:app --reload```

2. **Access the API documentation**:
    - Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.

## Endpoints

- `POST /extract_cv_info`: Upload a PDF CV to extract structured information.
- `POST /extract_job_info`: Extract structured information from job descriptions.

## Project Structure

 ```├── pycache/ ├── .env ├── .env.example ├── .gitignore ├── data/ │ ├── CVs/ │ ├── JDs/ │ └── Temp/ ├── main.py ├── output.csv ├── requirements.txt ├── source/ │ ├── configs/ │ │ ├── pycache/ │ │ └── db_connection.py │ ├── controller/ │ │ ├── pycache/ │ │ ├── CandidateManagement.py │ │ └── JobManagement.py │ ├── models/ │ │ ├── pycache/ │ │ ├── candidates.py │ │ └── jobs.py │ ├── routes/ │ │ ├── pycache/ │ │ ├── CandidateManagement.py │ │ └── JobManagement.py │ └── services/ │ ├── pycache/ │ ├── CV_Infor_Extraction.py │ └── Job_Info_Extraction.py ├── utils/ │ ├── pycache/ │ ├── llm.py │ └── preprocessed_text.py └── venv/ ├── etc/ ├── Include/ ├── Lib/ ├── pyvenv.cfg ├── Scripts/ └── share/``` 