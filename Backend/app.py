from fastapi import FastAPI, UploadFile, File
from search_engine import (
    recommend_from_uploaded_image,
    recommend_from_product
)
import os
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount(
    "/images",
    StaticFiles(directory="Images"),
    name="images"
)


@app.get("/")
def home():
    return {
        "message": "Fashion Recommendation API"
    }


@app.get("/recommend/{product_id}")
def recommend(product_id: int):

    recommendations = recommend_from_product(
        product_id
    )

    return {
        "product_id": product_id,
        "recommendations": recommendations
    }


@app.post("/upload-image")
async def upload_image(
    file: UploadFile = File(...)
):

    # create uploads folder if it doesn't exist
    os.makedirs(
        "uploads",
        exist_ok=True
    )

    save_path = os.path.join(
        "uploads",
        file.filename
    )

    with open(save_path, "wb") as f:
        f.write(
            await file.read()
        )

    recommendations = (
        recommend_from_uploaded_image(
            save_path
        )
    )

    return {
        "uploaded_file": file.filename,
        "recommendations": recommendations
    }