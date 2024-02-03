from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return "Welcome to the root path!"

@app.get("/ping")
async def ping():
    return "Hello, yash is here"

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Handle the uploaded file here
    return {"filename" : file.filename}

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
