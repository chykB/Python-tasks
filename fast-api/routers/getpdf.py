from fastapi import APIRouter, File, UploadFile
import os

router = APIRouter()

@router.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...), directory_path=None):
    """
        This endpoint collect a PDF file and saves it to the specified directory path. 
        Returns a dictionary indicating the success status and a message.
        malikchika86@gmail.com
    """
    try:
        filename, file_extension = os.path.splitext(file.filename)
        if file_extension.lower() != ".pdf":
            raise ValueError("Upload a pdf file")
        
        if directory_path:
            upload_directory = os.path.abspath(directory_path)
            os.makedirs(upload_directory, exist_ok=True)
        else: 
            upload_directory = os.path.abspath(".")

        file_path = os.path.join(upload_directory, file.filename)
        
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        return {"success": "File uploaded successfully"}
    except Exception as e:
        return {"error": str(e)}