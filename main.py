from fastapi import FastAPI, HTTPException, status

from routers.products import router as products_router
from settings.db import ping

app = FastAPI()
app.include_router(products_router)


@app.get("/")
async def read_root():
    return {"Hello": "World!"}


@app.get("/health_check", status_code=status.HTTP_200_OK)
async def db_healthcheck():
    is_alive = await ping()
    if not is_alive:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection failed",
        )
    return {"status": "healthy", "database": "connected"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
