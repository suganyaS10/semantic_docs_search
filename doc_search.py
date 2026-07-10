import voyageai
from dotenv import load_dotenv
import numpy as np

load_dotenv()

vo = voyageai.Client()

def cosine_similarity(a, b):
  a = np.array(a)
  b = np.array(b)
  return np.dot(a, b)/ (np.linalg.norm(a) * np.linalg.norm(b))

def normalize(vectors):
    v = np.array(vectors)
    # divide each row by its own length → every row now has length 1
    return v / np.linalg.norm(v, axis=1, keepdims=True)


docs = [
  "The Golden Retriever is a friendly, intelligent dog breed.",
  "To make espresso, force hot water through finely ground coffee.",
  "Python is a popular programming language for data science.",
  "Cats are independent animals that groom themselves.",
  "The Eiffel Tower is a landmark in Paris, France.",
  "Machine learning models learn patterns from data.",
  "A balanced diet includes fruits, vegetables, and protein.",
]

doc_vectors = vo.embed(
  docs,
  model="voyage-4",
  input_type="document"
).embeddings

doc_with_vectors = zip(docs, doc_vectors)

def search_query(query):
  query_vector = vo.embed(
    [query],
    model="voyage-4",
    input_type="query"
  ).embeddings[0]
  
  scored = []
  for doc, doc_vector in zip(docs, doc_vectors):
    score = cosine_similarity(query_vector, doc_vector)
    scored.append([score, doc])
  
  scored.sort(reverse=True)
  return scored[:3]

for query in ["how do I train my puppy?", "brewing a strong coffee", "what is AI?"]:
  results = search_query(query)
  for score, doc in results:
    print(f"{score} {doc}")

def fast_search_query(query):
  doc_matrix = normalize(doc_vectors)
  query_matrix = normalize(vo.embed(
    [query],
    model="voyage-4",
    input_type="query"
  ).embeddings[0])

  scores = doc_matrix @ query_matrix
  top = np.argsort(scores)[::-1][:3]

  return [(scores[i], docs[i]) for i in top]

for query in ["how do I train my puppy?", "brewing a strong coffee", "what is AI?"]:
  results = search_query(query)
  for score, doc in results:
    print(f"{score} {doc}")







      




