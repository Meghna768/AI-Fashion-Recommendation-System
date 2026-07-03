import numpy as np
import faiss

embeddings = np.load(
    "hybrid_embeddings.npy"
)

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(
    embeddings
)

faiss.write_index(
    index,
    "hybrid.index"
)

print(
    "Vectors:",
    index.ntotal
)