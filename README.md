# Semantic Document Search — learning embeddings with Voyage AI

A hands-on walk from raw embeddings to a small Retrieval-Augmented Generation (RAG)
app, built step by step to understand how embeddings power semantic search.

## The progression

| File | What it demonstrates |
|------|----------------------|
| `first_embeddings.py` | Turn text into a vector with Voyage; inspect the raw numbers and dimensions |
| `measure_similarity.py` | Cosine similarity — measuring closeness of meaning between texts |
| `doc_search.py` | Semantic search: embed a document set, embed a query, rank by similarity |
| `mini_rag.py` | RAG: retrieve relevant docs, then have Claude answer grounded only in that context |

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install voyageai numpy anthropic

cp .env.example .env   # then add your keys
```

Load the keys into your shell (or use a dotenv loader), then run any script:

```bash
python3 doc_search.py
```

## Concepts covered

- **Embeddings** — text → fixed-length vector; similar meaning → similar vector
- **Cosine similarity** — comparing direction, not magnitude
- **Semantic search** — ranking documents by meaning, not keywords
- **RAG** — grounding an LLM's answer in retrieved context

Uses Voyage AI (`voyage-4`) for embeddings and Claude (`claude-opus-4-8`) for generation.
