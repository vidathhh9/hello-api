# Hello API

A small FastAPI service, packaged with Docker, that returns simple features of a URL (length, HTTPS use, dot count). It is the first step towards a phishing URL detector.

## Run it

Requires Docker only.

```bash
git clone https://github.com/vidathhh9/hello-api.git
cd hello-api
docker compose up --build
```

Then open http://localhost:8000/docs to try it.

## Endpoints

- `GET /health` returns `{"status": "ok"}`
- `POST /features` takes `{"url": "..."}` and returns its features

## What it shows

- Input validation: empty and oversized URLs are rejected with a 422 error
- Automated tests with pytest
- A small container image that runs as a non-root user
- Docker Compose with the port published to localhost only
