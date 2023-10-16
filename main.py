from fastapi import FastAPI
from models import SolutionInput
from business_logic import process_orders
from settings import Settings
import aioredis
import datetime


app = FastAPI(title="FastAPI Fonoma test")

redis_cache = None 

@app.on_event("startup")
async def startup():
    settings = Settings()

    global redis_cache
    redis_cache = await aioredis.create_redis_pool(
        f"redis://{settings.redis_host}:{settings.redis_port}"
    )

@app.on_event("shutdown")
async def shutdown():
    global redis_cache
    if redis_cache is not None:
        redis_cache.close()
        await redis_cache.wait_closed()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/solution")
async def solution(input: SolutionInput):
    cache_key = str(input) 
    response = await redis_cache.get(cache_key)
    if not response:
        response = process_orders(input.orders, input.criterion)
        await redis_cache.setex(cache_key, datetime.timedelta(days=1).total_seconds(), response)
    
    return response

