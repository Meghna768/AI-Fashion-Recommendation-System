from sentence_transformers import SentenceTransformer
from PIL import Image
import numpy as np
import pandas as pd
import os

df = pd.read_csv("Fashion Dataset.csv")

model = SentenceTransformer("clip-ViT-B-32")

embeddings = []
valid_indices = []

count = 0

for idx in range(len(df)):

    image_path = f"Images/{idx}.jpg"

    if not os.path.exists(image_path):
        continue

    try:
        img = Image.open(image_path)

        embedding = model.encode(img)

        embeddings.append(embedding)
        valid_indices.append(idx)

        count += 1

        if count % 100 == 0:
            print(f"Processed {count} images")

        if count == 1000:
            break

    except Exception as e:
        print(f"Error with image {idx}: {e}")

embeddings = np.array(embeddings)
valid_indices = np.array(valid_indices)

np.save("image_embeddings.npy", embeddings)
np.save("valid_indices.npy", valid_indices)

print("Saved Successfully")
print("Shape:", embeddings.shape)