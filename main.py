from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    try:
        content = await file.read()
        text = content.decode("utf-8")  

        return JSONResponse({"message": "Document uploaded successfully", "filename": file.filename})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
