import asyncio
import logging
from fastapi import HTTPException, status, FastAPI
import random

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/ping")
async def health_check():

    logger.info(" INFO logging test ")
    logger.warning(" WARNING test ")
    logger.error(" ERROR log test")

    return "ping"

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if item_id % 2 == 0:
        # mock io - wait for x seconds
        seconds = random.uniform(0, 3)
        await asyncio.sleep(seconds)
    return {"item_id": item_id, "q": q}


@app.get("/invalid")
async def invalid():
    logger.warning("This is message /invalid")
    raise ValueError("Invalid ")

@app.get("/exception")
async def exception():
    try:
        raise ValueError("exception")
    except Exception as ex:
        # generate random number
        seconds = random.uniform(0, 30)
        # Create the exception. 
        exception = IOError("Failed at " + str(seconds))
        # Update status to failed.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"HTTP 500 internal server error")