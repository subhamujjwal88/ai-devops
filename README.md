# DevOps Practice Project - Phase 1

Welcome to Phase 1 of your step-by-step DevOps practice project.

The goal of this phase is to establish a working Python web application and an automated test suite running locally on your machine before introducing containerization, CI/CD, or orchestration.

---

## 1. Project Structure

```text
.
├── app/
│   ├── __init__.py
│   └── main.py          # FastAPI application with core endpoints
├── tests/
│   ├── __init__.py
│   └── test_main.py     # Automated tests using pytest
├── .gitignore           # Excludes virtual environments and cache files
├── requirements.txt     # Python dependencies
└── README.md            # Phase 1 documentation
```

---

## 2. Getting Started (Step-by-Step)

### Step 1: Create a Python Virtual Environment

A virtual environment isolates this project's dependencies from your system Python.

```bash
python3 -m venv .venv
```

### Step 2: Activate the Virtual Environment

- **Linux / macOS:**
  ```bash
  source .venv/bin/activate
  ```

Once activated, your terminal prompt will show `(.venv)`.

### Step 3: Install Dependencies

Install FastAPI, Uvicorn, Pytest, and HTTPX:

```bash
pip install -r requirements.txt
```

---

## 3. Running the Application

Start the local development server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The `--reload` flag automatically reloads the server when you make changes to Python files.

Once the server starts, test the endpoints:
- **Root greeting:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Health check:** [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)
- **App info:** [http://127.0.0.1:8000/info](http://127.0.0.1:8000/info)
- **Interactive API Docs (Swagger):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

You can also test with `curl` from a separate terminal:

```bash
curl http://127.0.0.1:8000/health
```

Output:
```json
{"status":"healthy"}
```

---

## 4. Running the Tests

To verify that your code works as expected, run the test suite:

```bash
pytest -v
```

Expected output:
```text
tests/test_main.py::test_read_root PASSED
tests/test_main.py::test_health_check PASSED
tests/test_main.py::test_app_info PASSED
```

---

## 5. What's Coming in Next Phases

- **Phase 2: Docker**: Packaging this application into an isolated container image.
- **Phase 3: CI Pipeline**: Automating linting and `pytest` with GitHub Actions on every push.
- **Phase 4: Docker Compose**: Adding a backing service (e.g., Redis) and managing multiple containers.
- **Phase 5: Kubernetes**: Deploying the container into a local K8s cluster (Minikube/kind/k3s) with health probes.
