from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Kitty Tutor API is running!"}
