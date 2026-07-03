import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

df = pd.read_csv("Fashion Dataset.csv")

df["name"] = df["name"].fillna("")
df["brand"] = df["brand"].fillna("")
df["colour"] = df["colour"].fillna("")
df["description"] = df["description"].fillna("")

df["search_text"] = (
    df["name"]
    + " "
    + df["brand"]
    + " "
    + df["colour"]
    + " "
    + df["description"]
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

texts = df["search_text"][:1000].tolist()

text_embeddings = model.encode(
    texts,
    show_progress_bar=True
)

text_embeddings = np.array(text_embeddings)

np.save(
    "text_embeddings.npy",
    text_embeddings
)

print("Shape:", text_embeddings.shape)