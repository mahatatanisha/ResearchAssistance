from fastapi import APIRouter, UploadFile, File
from typing import List
from modules.load_vectorstore import load_vectorstore
from fastapi.responses import JSONResponse
from logger import logger

router=APIRouter()

@router.post("/upload_pdfs/")
async def upload_pdfs(files:List[UploadFile]=File(...)):
    try:
        logger.info("Recieved uploaded files")
        load_vectorstore(files)
        logger.info("succesfully added to vectorstore!")
    except Exception as e:
        logger.exception("Error during upload")
        return JSONResponse(status_code=500,content={"error":str(e)})