from transformers import AutoTokenizer, AutoModel
import torch
import pandas as pd
import numpy as np

print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(
    "sentence-transformers/all-MiniLM-L6-v2"
)

model = AutoModel.from_pretrained(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Model loaded")


df = pd.read_csv("Fashion Dataset.csv")

df["name"] = df["name"].fillna("")
df["brand"] = df["brand"].fillna("")
df["colour"] = df["colour"].fillna("")
df["description"] = df["description"].fillna("")

texts = []

for i in range(1000):

    text = (
        str(df.iloc[i]["name"]) + " "
        + str(df.iloc[i]["brand"]) + " "
        + str(df.iloc[i]["colour"]) + " "
        + str(df.iloc[i]["description"])
    )

    texts.append(text)

text_embeddings = []

for i, text in enumerate(texts):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():

        outputs = model(**inputs)

        embedding = outputs.last_hidden_state.mean(dim=1)

    text_embeddings.append(
        embedding.squeeze().numpy()
    )

    if (i + 1) % 100 == 0:
        print(f"Processed {i+1}")

text_embeddings = np.array(text_embeddings)

np.save(
    "text_embeddings.npy",
    text_embeddings
)

print("Saved")
print(text_embeddings.shape)