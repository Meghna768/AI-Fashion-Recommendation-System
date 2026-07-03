import numpy as np
import faiss

embeddings = np.load("image_embeddings.npy")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(
    index,
    "fashion.index"
)

print("Index created")
print("Vectors:", index.ntotal)