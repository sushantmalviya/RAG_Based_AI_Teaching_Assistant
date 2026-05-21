import joblib
import requests
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import numpy as np

def create_embedding(text_list):        
    r = requests.post("http://localhost:11434/api/embed",
                    json={
                        "model" : "bge-m3",
                        "input" : text_list
                    }) 

    embedding = r.json()["embeddings"]

    return embedding


df = joblib.load("embeddings.joblib")

df1 = df[:10]
incoming_query = input("Ask your question:")
question_embedding = create_embedding(incoming_query)[0]

print(question_embedding)

similarities = cosine_similarity(np.vstack(df1['embedding']), [question_embedding]).flatten()
print(similarities)
top_results = 3
max_idx = similarities.argsort()[::-1][0:top_results]
print(max_idx)

new_df = df1.loc[max_idx]
print(new_df[["title", "number", "text"]])
