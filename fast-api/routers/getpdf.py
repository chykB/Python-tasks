from fastapi import APIRouter, File, UploadFile
import os

router = APIRouter()

@router.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...), directory_path=None, overwrite_existing=False):
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

        if os.path.exists(file_path):
            if overwrite_existing:
                with open(file_path, "wb") as f:
                    f.write(file.file.read())
                return {"success": "File overwritten successfully"}
            else:
                return {"prompt": f"File already exist at this location: {file_path}. Do you want to overwrite it or choose a different directory"}
        else:
            with open(file_path, "wb") as f:
                f.write(file.file.read())

            return {"success": "File uploaded successfully"}
    except Exception as e:
        return {"error": str(e)}