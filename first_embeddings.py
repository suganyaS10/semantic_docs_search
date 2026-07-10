import voyageai
from dotenv import load_dotenv

load_dotenv()
va = voyageai.Client()

text = "I adore puppies"

result = va.embed(
  [text],
  model="voyage-4",
  input_type="document"
)

vector = result.embeddings[0]

print("type:", type(vector))
print("length:", len(vector))
print("first 8 chars:", vector[:8])
print("tokens used:", result.total_tokens)

