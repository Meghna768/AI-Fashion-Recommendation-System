import numpy as np

image_embeddings = np.load(
    "image_embeddings.npy"
)

text_embeddings = np.load(
    "text_embeddings.npy"
)

image_embeddings = (
    image_embeddings /
    np.linalg.norm(
        image_embeddings,
        axis=1,
        keepdims=True
    )
)

text_embeddings = (
    text_embeddings /
    np.linalg.norm(
        text_embeddings,
        axis=1,
        keepdims=True
    )
)

hybrid_embeddings = np.concatenate(
    [
        0.7 * image_embeddings,
        0.3 * text_embeddings
    ],
    axis=1
)

np.save(
    "hybrid_embeddings.npy",
    hybrid_embeddings
)

print(
    hybrid_embeddings.shape
)