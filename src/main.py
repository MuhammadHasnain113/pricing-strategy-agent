import os
from fastapi import FastAPI
from src.api.v1.pricing import router as pricing_router
from src.api.v1.health import router as health_router

app = FastAPI(title="Pricing Strategy Agent (PSA)")

app.include_router(health_router, prefix="/health")
app.include_router(pricing_router, prefix="/api/v1/pricing")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
