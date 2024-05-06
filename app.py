from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os
from minup import MinioUpload

app = FastAPI()

# Upload the image
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join("/home/parmida", file.filename)
    minio_upload = MinioUpload(url="static.snpxdev.com", access_key="uXQ5Dk0in18El2F1F79H", secret_key="litiS53Pn4ObapMVr3mOhubi9mEIrjXLhUstKQps", bucket_name="test-parmida", http_prefix="https")
    uploaded_image_url = minio_upload.upload_image(file_path)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": uploaded_image_url}

# Retrieve the image
@app.get("/get_image/{file_name}")
async def get_image(file_name: str):
    file_path = os.path.join("/home/parmida", file_name)
    return FileResponse(file_path, media_type="image/jpeg")
