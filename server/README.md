# Job Resume Matching Project

- This project extracts structured information from CVs and JDs using FastAPI and LangChain.
- Use the extracted information to determine the number of CVs that match the job descriptions.

## Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)

## Setup

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Copy `.env.example` to `.env`:
    ```sh
    cp .env.example .env
    ```
    - Edit `.env` to include your `LLAMA_3_API_KEY`, `MONGODB_URI`, and `MONGODB_DB`.

## Running the Application

1. **Start the FastAPI server**:
    ```sh
    uvicorn main:app --reload
    ```

2. **Access the API documentation**:
    - Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation.

## Connecting to MongoDB

1. **Ensure MongoDB is running**:
    - If you are using a local MongoDB instance, make sure it is running.
    - If you are using a cloud MongoDB service (e.g., MongoDB Atlas), ensure you have the connection string.

2. **Configure MongoDB connection**:
    - In the `.env` file, set the `MONGODB_URI` to your MongoDB connection string.
    - Set the `MONGODB_DB` to the name of your database.

    Example `.env` file:
    ```env
    LLAMA_3_API_KEY=your_llama_3_api_key
    MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
    MONGODB_DB=your_database_name
    ```

## License

This project is licensed under the MIT License.