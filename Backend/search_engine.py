import numpy as np
import faiss
import pandas as pd
from PIL import Image
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("clip-ViT-B-32")

df = pd.read_csv("Fashion Dataset.csv")

valid_indices = np.load(
    "valid_indices.npy"
)

# HYBRID SYSTEM
hybrid_embeddings = np.load(
    "hybrid_embeddings.npy"
)

hybrid_index = faiss.read_index(
    "hybrid.index"
)

# IMAGE SYSTEM
image_embeddings = np.load(
    "image_embeddings.npy"
)

image_index = faiss.read_index(
    "fashion.index"
)

def recommend_from_product(product_idx, top_k=5):

    D, I = hybrid_index.search(
    hybrid_embeddings[product_idx].reshape(1, -1),
    top_k + 1
)

    recommendations = []

    for emb_idx in I[0][1:]:

        actual_idx = valid_indices[emb_idx]

        recommendations.append(
    {
        "name": df.iloc[actual_idx]["name"],
        "brand": df.iloc[actual_idx]["brand"],
        "price": float(df.iloc[actual_idx]["price"]),
        "image": f"{actual_idx}.jpg"
    }

)
    return recommendations
def get_image_embedding(path):

    img = Image.open(path)

    embedding = model.encode(img)

    return embedding
def recommend_from_uploaded_image(
    image_path,
    top_k=5
):

    query_embedding = get_image_embedding(
        image_path
    )

    D, I = image_index.search(
    query_embedding.reshape(1, -1),
    top_k
)

    recommendations = []

    for emb_idx in I[0]:

        actual_idx = valid_indices[emb_idx]

        recommendations.append(
    {
        "name": df.iloc[actual_idx]["name"],
        "brand": df.iloc[actual_idx]["brand"],
        "price": float(df.iloc[actual_idx]["price"]),
        "image": f"{actual_idx}.jpg"
    }
)
    return recommendations