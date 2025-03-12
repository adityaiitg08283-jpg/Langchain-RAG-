from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

doc_embeddings = np.array(embedding.embed_documents(documents))
query_embedding = np.array(embedding.embed_query(query)).reshape(1,384)

sim_score = cosine_similarity(doc_embeddings,query_embedding)

# Optimized Code
print(np.argmax(sim_score)) # prints the index with maximum similarity score
print(documents[np.argmax(sim_score)]) # prints the most similar sentence


'''****************************'''

# Code in Youtube Lecture

# scores = cosine_similarity([query_embedding], doc_embeddings)[0]
# index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
# print(query)
# print(documents[index])
# print("similarity score is:", score)