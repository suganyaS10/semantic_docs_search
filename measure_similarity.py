import voyageai
from dotenv import load_dotenv
import numpy as np

load_dotenv()

vo = voyageai.Client()

def cosine_similarity(a, b):
  a = np.array(a)
  b = np.array(b)
  return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

anchor = "I loge dogs"
candidates = [
  "I adore puppies",
  "Cat is a wonderful pet",
  "Sky cannot be orange"
]

vectors = vo.embed(
  [anchor] + candidates,
  model="voyage-4",
  input_type="document"
).embeddings

anchor_vector = vectors[0]

for sentence, vector in zip(candidates, vectors[1:]):
  score = cosine_similarity(anchor_vector, vector)
  print(f"{score:.3f} - {sentence}")  

