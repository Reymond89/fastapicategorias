from fastapi import FastAPI
from routers.categoria import category

app = FastAPI()

app.include_router(category)