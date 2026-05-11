from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from models import HealthResponse

# Aplikace + jediny stav serveru: jedna instance pizzerie.

app = FastAPI(title="Knihovna API", version="1.0.0")
#knihovna = Knihovna()


# ============================================================
# SHUTDOWN CALLBACK
# ============================================================

@app.on_event("shutdown")
def shutdown_event():
    """Callback method executed when the server is shutting down."""
    print("Server je vypínán...")
    # Add cleanup code here (e.g., closing database connections, saving state, etc.)


# ============================================================
# ENDPOINTY
# ============================================================

@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")
