from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Hello API")


class UrlRequest(BaseModel):
    url: str = Field(min_length=1, max_length=2048)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/features")
def features(req: UrlRequest):
    url = req.url.strip().lower()
    return {
        "url": url,
        "url_length": len(url),
        "uses_https": url.startswith("https"),
        "dot_count": url.count("."),
    }