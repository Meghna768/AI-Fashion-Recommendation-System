import numpy as np
import faiss
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv("Fashion Dataset.csv")

embeddings = np.load("image_embeddings.npy")
valid_indices = np.load("valid_indices.npy")

index = faiss.read_index("fashion.index")

query_idx = 0

D, I = index.search(
    embeddings[query_idx].reshape(1, -1),
    6
)

query_actual_idx = valid_indices[query_idx]

print("Query Product:")
print(df.iloc[query_actual_idx]["name"])

plt.figure(figsize=(20, 5))

for pos, emb_idx in enumerate(I[0]):

    actual_idx = valid_indices[emb_idx]

    img = Image.open(
        f"Images/{actual_idx}.jpg"
    )

    plt.subplot(1, 6, pos + 1)
    plt.imshow(img)
    plt.axis("off")

    title = df.iloc[actual_idx]["name"][:25]

    if pos == 0:
        plt.title("QUERY\n" + title)
    else:
        plt.title(f"TOP {pos}\n" + title)

plt.tight_layout()
plt.show()