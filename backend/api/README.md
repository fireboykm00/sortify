# File Organizer API

A FastAPI-based API for organizing and categorizing uploaded files.

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the virtual environment:

- Windows:

```bash
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create an uploads directory:

```bash
mkdir uploads
```

5. Run the API from the root directory:
+
```bash
cd ..
uvicorn api.main:app --reload
```

The API will be available at `http://localhost:8000` with the docs at `http://localhost:8000/docs`.

## API Endpoints

- `POST /files`: Upload and organize files
- `GET /download/{session_id}`: Download organized files as ZIP
- `GET /`: Health check endpoint
