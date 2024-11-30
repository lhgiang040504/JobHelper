# Job Resume Matching Project

- This project extracts structured information from CVs and JDs using FastAPI and LangChain.
- Use the extracted information to determine the number of CVs that match the job descriptions.

## Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)

## Setup

1. **Clone the repository**:
    ```
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment**:
    ```
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Copy `.env.example` to `.env`:
    ```
    cp .env.example .env
    ```
    - Edit `.env` to include your `LLAMA_3_API_KEY`, `MONGODB_URI`, and `MONGODB_DB`.

## Running the Application

1. **Start the FastAPI server**:
    ```
    uvicorn main:app --reload
    ```

2. **Access the API documentation**:
    - Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.

## Endpoints

- `POST /extract_cv_info`: Upload a PDF CV to extract structured information.
- `POST /extract_job_info`: Extract structured information from job descriptions.

## License

This project is licensed under the MIT License.