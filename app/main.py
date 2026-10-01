from fastapi import FastAPI

app = FastAPI(
    title = "Subscription AI Agent",
    version = "1.0.0"
)

@app.get("/health")
def health():

    return {
        "status": "UP"
    }