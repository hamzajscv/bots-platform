from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "مرحبا بك! سيرفر البوتات خدام مزيان."}