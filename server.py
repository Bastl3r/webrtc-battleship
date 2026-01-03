from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import random

# Initialize FastAPI app for JSON caching API and static files
app = FastAPI()

# Allow all origins for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory cache for SDP shortening
cache = {}

def generate_numeric_key():
    """Generates a zero-padded 6-digit number, e.g. '042391'"""
    return f"{random.randint(0, 999999):06d}"

@app.post("/store")
async def store_json(request: Request):
    """Store JSON data and return a numeric key"""
    data = await request.json()
    key = generate_numeric_key()

    # Avoid collisions
    while key in cache:
        key = generate_numeric_key()

    cache[key] = data
    return {"key": key}

@app.get("/retrieve/{key}")
async def retrieve_json(key: str):
    """Retrieve stored JSON data by key"""
    if key not in cache:
        return {"error": "Key not found"}

    # Return the stored JSON exactly as it was provided
    return cache[key]

@app.post("/store/{key}")
async def overwrite_json(key: str, request: Request):
    """Overwrite stored JSON data with a new value (e.g., answer SDP overwriting offer SDP)"""
    if key not in cache:
        return {"error": "Key not found"}
    
    data = await request.json()
    cache[key] = data
    return {"success": True, "key": key}

# Mount static files (HTML, CSS, JS) - must be last
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    # Run FastAPI/Uvicorn with HTTPS on port 8443
    print("Starting server on HTTPS port 8443...")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8443,
        ssl_keyfile="key.pem",
        ssl_certfile="cert.pem",
        log_level="info"
    )
