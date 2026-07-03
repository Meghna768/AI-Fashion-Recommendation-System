import pandas as pd
df=pd.read_csv("Fashion Dataset.csv")
#drop null values as they less compares to the dataset we have
df = df.dropna(
    subset=[
        "name",
        "brand",
        "description"
    ]
)
#print(df.shape)
#for columns having more null (rating) make it 0
df["ratingCount"] = df["ratingCount"].fillna(0)
df["avg_rating"] = df["avg_rating"].fillna(0)
#cleaning descriptions by removing tags
import re
def clean_text(text):
    text = re.sub(r"<.*?>", " ", str(text))
    return text.strip()

df["description"] = df["description"].apply(clean_text)
#making a text field later for embeddings
df["search_text"] = (
    df["name"].astype(str)
    + " "
    + df["brand"].astype(str)
    + " "
    + df["colour"].fillna("").astype(str)
    + " "
    + df["description"].astype(str)
)
import os

count = 0

for i in range(len(df)):
    if os.path.exists(f"Images/{i}.jpg"):
        count += 1

print("Images found:", count)
print("Rows:", len(df))