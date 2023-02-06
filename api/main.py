from fastapi import FastAPI
from routes.user_route import user_router
from routes.token_route import token_router

app = FastAPI()

app.include_router(user_router)
app.include_router(token_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
