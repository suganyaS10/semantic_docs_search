import re

document = """The Golden Retriever is a friendly and intelligent dog breed. \
They were originally bred in Scotland in the mid-19th century for retrieving \
game during hunting. Golden Retrievers need at least two hours of exercise per \
day and are known for their gentle temperament, making them excellent family pets.

Espresso is a concentrated coffee brewed by forcing hot water through finely \
ground coffee beans at about nine bars of pressure. A single shot uses roughly \
seven to nine grams of coffee and extracts in twenty-five to thirty seconds. \
The result is a thick beverage topped with a reddish-brown foam called crema.

The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris. \
It was designed by Gustave Eiffel and completed in 1889 for the World's Fair. \
Standing 330 metres tall, it was the tallest man-made structure in the world \
until the Chrysler Building was finished in New York in 1930."""

def chunk_by_chars(text, char_size=20):
  start_index = 0
  chunks = []
  while start_index < len(text):
      chunks.append(text[start_index:start_index + char_size])
      start_index += char_size
      return chunks
  
def split_sentences(paragraph):
  parts = re.split(r'(?<=[.!?]) ', paragraph.replace("\n", " "))
  return [p.strip() for p in parts if p.strip()]  
  
def chunk_document(document, chunk_size=250):
  chunks = []
  paragraphs = document.split("\n\n")

  for paragraph in paragraphs:
    paragraph = paragraph.strip()
    if not paragraph:
      continue
    sentences = split_sentences(paragraph)
    current_chunk = []
    for sentence in sentences:
      if current_chunk and len(" ".join(current_chunk + [sentence])) > chunk_size:
        chunks.append(" ".join(current_chunk))
        current_chunk = current_chunk[-1:]
      current_chunk.append(sentence)
    if current_chunk:
      chunks.append(" ".join(current_chunk))

  return chunks

# def chunk_document(document, chunk_size=250, overlap_sentences=1):
#     chunks = []
#     for paragraph in document.split("\n\n"):
#         paragraph = paragraph.strip()
#         if not paragraph:
#             continue
#         current = []                       # sentences in the chunk being built
#         for sentence in split_sentences(paragraph):
#             # would adding this sentence overflow the size cap?
#             if current and len(" ".join(current + [sentence])) > chunk_size:
#                 chunks.append(" ".join(current))          # flush the full chunk
#                 current = current[-overlap_sentences:]    # seed next chunk with the tail
#             current.append(sentence)
#         if current:
#             chunks.append(" ".join(current))              # flush the remainder
#     return chunks

chunk_by_chars(document)

chunks = chunk_document(document)
print("Length of chunks: ", len(chunks))
for i, c in enumerate(chunks):
  print(f"--- chunk {i} ({len(c)} chars) ---")
  print(c)
  print()


