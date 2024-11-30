# CV Information Extraction

This project extracts structured information from CVs using FastAPI and LangChain.

## Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)

## Setup

1. **Clone the repository**:
    \`\`\`sh
    git clone <repository-url>
    cd <repository-directory>
    \`\`\`

2. **Create and activate a virtual environment**:
    \`\`\`sh
    python -m venv venv
    source venv/bin/activate  # On Windows use \[activate](http://_vscodecontentref_/1)
    \`\`\`

3. **Install dependencies**:
    \`\`\`sh
    pip install -r requirements.txt
    \`\`\`

4. **Set up environment variables**:
    - Copy \`.env.example\` to \`.env\`:
        \`\`\`sh
        cp [.env.example](http://_vscodecontentref_/2) .env
        \`\`\`
    - Edit \`.env\` to include your \`LLAMA_3_API_KEY\`, \`MONGODB_URI\`, and \`MONGODB_DB\`.

## Running the Application

1. **Start the FastAPI server**:
    \`\`\`sh
    uvicorn main:app --reload
    \`\`\`

2. **Access the API documentation**:
    - Open your browser and go to \`http://127.0.0.1:8000/docs\` to see the interactive API documentation.

## Endpoints

- \`POST /extract_cv_info\`: Upload a PDF CV to extract structured information.
- \`POST /extract_job_info\`: Extract structured information from job descriptions.

## Project Structure

\`\`\`
.
├── __pycache__/
├── .env
├── [.env.example](http://_vscodecontentref_/3)
├── .gitignore
├── data/
│   ├── CVs/
│   ├── JDs/
│   └── Temp/
├── [main.py](http://_vscodecontentref_/4)
├── [output.csv](http://_vscodecontentref_/5)
├── requirements.txt
├── source/
│   ├── configs/
│   │   ├── __pycache__/
│   │   └── db_connection.py
│   ├── controller/
│   │   ├── __pycache__/
│   │   ├── CandidateManagement.py
│   │   └── JobManagement.py
│   ├── models/
│   │   ├── __pycache__/
│   │   ├── candidates.py
│   │   └── jobs.py
│   ├── routes/
│   │   ├── __pycache__/
│   │   ├── CandidateManagement.py
│   │   └── JobManagement.py
│   └── services/
│       ├── __pycache__/
│       ├── CV_Infor_Extraction.py
│       └── Job_Info_Extraction.py
├── utils/
│   ├── __pycache__/
│   ├── llm.py
│   └── preprocessed_text.py
└── venv/
    ├── etc/
    ├── Include/
    ├── Lib/
    ├── pyvenv.cfg
    ├── Scripts/
    └── share/
\`\`\`

## License

This project is licensed under the MIT License.