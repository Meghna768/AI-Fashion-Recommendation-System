import numpy as np
import faiss
import pandas as pd

df = pd.read_csv("Fashion Dataset.csv")

embeddings = np.load("embedding/image_embeddings.npy")

index = faiss.read_index("fashion.index")

query = embeddings[0]

D, I = index.search(
    query.reshape(1, -1),
    5
)

print("Indices:")
print(I)

print("\nProducts:")

for idx in I[0]:
    print(df.iloc[idx]["name"])