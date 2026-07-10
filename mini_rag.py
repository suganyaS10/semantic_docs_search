import voyageai
from anthropic import Anthropic
from dotenv import load_dotenv
import numpy as np

load_dotenv()

anthropic = Anthropic()
vo = voyageai.Client()

def normalize(vectors):
    v = np.array(vectors)
    # divide each row by its own length → every row now has length 1
    return v / np.linalg.norm(v, axis=1, keepdims=True)

docs = [
    "The Golden Retriever is a friendly, intelligent dog breed that needs daily exercise.",
    "To make espresso, force hot water at 9 bars of pressure through finely ground coffee.",
    "Python is a popular programming language for data science and machine learning.",
    "Cats are independent animals that groom themselves and sleep 12-16 hours a day.",
    "The Eiffel Tower in Paris is 330 metres tall and was completed in 1889.",
    "Machine learning models learn patterns from data rather than being explicitly programmed.",
]

doc_vecors = vo.embed(
    docs,
    model="voyage-4",
    input_type="document"
).embeddings

doc_matrix = normalize(doc_vecors)

def retrieve(query):
    query_vector = vo.embed(
        [query],
        model="voyage-4",
        input_type="query"
      ).embeddings
    
    query_matrix = normalize(query_vector)[0]
    scores = doc_matrix @ query_matrix
    doc_indices = np.argsort(scores)[::-1][:3]
    return [docs[doc_index] for doc_index in doc_indices]

def answer(query):
    context_docs = retrieve(query)
    context = "\n".join(f"- {doc}" for doc in context_docs)

    prompt = f"""Answer the question using ONLY the context below.
If the context doesn't contain the answer, say "I don't know based on the provided context."

Context:
{context}

Question: {query}"""
    
    response = anthropic.messages.create(
        model="claude-opus-4-8",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    text = next(b.text for b in response.content if b.type == "text")
    return text, context_docs

for q in ["how much exercise does a golden retriever need?",
          "what year was the eiffel tower finished?",
          "who won the world cup in 2018?"]:
    text, used = answer(q)
    print(f"\nQ: {q}")
    print(f"[retrieved: {len(used)} docs]")
    print(f"A: {text}")
        
