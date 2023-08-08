from fastapi import FastAPI
import uvicorn
from src.routes import contacts


app = FastAPI()

app.include_router(contacts.router, prefix='/api')


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
