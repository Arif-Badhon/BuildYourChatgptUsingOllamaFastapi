# 💬 Gemma3 Local Chat — FastAPI & Ollama Portfolio App

A lightning-fast local AI chat app using FastAPI, Python, and Ollama running Google Gemma3—streaming responses, ready for your portfolio, side projects, or prototypes!

![demo screenshot](static/demo.png)

## 🚀 Features

- **Local LLM:** Runs Google Gemma3 (`gemma3:1b`, `4b`, etc.) on your own hardware using Ollama.
- **FastAPI backend:** Optimized API with streaming responses for instant token display.
- **Zero-JS frontend:** Minimal HTML/JS for chat and live model replies—no frameworks needed.
- **Easy deployment:** Lockfile-based dependency management using [uv](https://astral.sh/uv/).
- **Docker-ready:** Provided Dockerfile for reproducible builds, local development, or cloud/server hosting.
- **Editable prompts:** Full chat history, adjustable system prompt, model tag, and sampling controls.
- **OpenAI-compatible option:** Use with OpenAI client SDKs for future cloud portability.

## 📦 Quickstart

> **Requirements:**  
> - Python 3.11+  
> - [Ollama](https://ollama.com/) installed & running locally  
> - `uv` Python package manager (recommended)
> - `gemma3` model pulled (e.g., `ollama pull gemma3:1b`)

#### 1. Clone & setup

git clone https://github.com/yourUsername/gemma3-fastapi-app.git
cd gemma3-fastapi-app
uv sync # installs dependencies from lockfile


#### 2. Ensure Ollama is running

ollama list # check installed models
ollama serve # optional, if not already running


#### 3. Run the app


Or for production:

uv run uvicorn app.main:app --host 0.0.0.0 --port 8000


#### 4. Chat!

Open [http://localhost:8000/static/index.html](http://localhost:8000/static/index.html)  
Type your message, get streaming Gemma3 responses!

## 🖥️ Project Structure

├── app/
│ └── main.py # FastAPI backend
├── static/
│ └── index.html # Frontend UI
│ └── demo.png # App screenshot
├── pyproject.toml
├── uv.lock
├── Dockerfile
├── README.md
└── CONTRIBUTE.md


## 🤩 Screenshots

![chat UI](static/demo.png)

## 🛠️ Config & Upgrades

- **Change model:** `gemma3:1b`, `gemma3:4b`, etc. — update in frontend or backend `main.py`.
- **Edit system prompt:** Set in frontend JS `history` array.
- **Add features:** Tool calling, PDF/RAG upload, or OpenAI-compatible endpoints—see [CONTRIBUTE.md](CONTRIBUTE.md).

## 👩‍💻 Built With

- FastAPI
- Ollama Python Client
- Google Gemma3 Model
- uv (Python Package Manager)
- Vanilla JavaScript (frontend)

## 📣 Contributions

All contributions, ideas, bug reports, and PRs are welcome!  
See [CONTRIBUTE.md](CONTRIBUTE.md) for full instructions.

## 📝 License

MIT — free for personal, educational, and professional use.

---

