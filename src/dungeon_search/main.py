import os
import sqlite3
from sqlite_vec import serialize_float32

import sqlite_vec
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
LOCAL_LLM = os.getenv('LOCAL_LLM')
LLM_MODEL = os.getenv('LLM_MODEL') or 'hermes-3-llama-3.1-8b'
client = OpenAI(
    base_url=LOCAL_LLM,
    api_key='not-needed'
)
db_path = 'documents.db'

db = sqlite3.connect(db_path)
db.enable_load_extension(True)
sqlite_vec.load(db)
db.enable_load_extension(False)

# db.execute('''
#    CREATE VIRTUAL TABLE documents USING vec0(
#        embedding float[768],
#        +file_name TEXT,
#        +content TEXT
#    )
# ''')
def get_openai_embedding(text):
   response = client.embeddings.create(
       model="text-embedding-nomic-embed-text-v1.5",
       input=text
   )
   return response.data[0].embedding

for file_name in os.listdir("docs"):
   file_path = os.path.join("docs", file_name)
   with open(file_path, 'r', encoding='utf-8') as file:
       content = file.read()
       # Generate embedding for the content
       embedding = get_openai_embedding(content)
       if embedding:
           # Insert file content and embedding into the vec0 table
           db.execute(
               'INSERT INTO documents (embedding, file_name, content) VALUES (?, ?, ?)',
               (serialize_float32(embedding), file_name, content))
# Commit changes
db.commit()



query_text = "Tell me more about the character my-dude?"
query_embedding = get_openai_embedding(query_text)
if query_embedding:
   rows = db.execute(
       """
       SELECT
           file_name,
           content,
           distance
       FROM documents
       WHERE embedding MATCH ?
       ORDER BY distance
       LIMIT 3
       """,
       [serialize_float32(query_embedding)]
   ).fetchall()
   print("Top 3 most similar documents:")
   top_contexts = []
   for row in rows:
       print(row)
       top_contexts.append(row[1])

context = "\n\n".join(top_contexts)
system_message = "You are a helpful assistant. Use the following context to answer the query by only using information within the document. Be short and sweet."
# Send query and context to OpenAI
try:
   completion = client.chat.completions.create(
       model=LLM_MODEL,
       messages=[
           {"role": "system", "content": system_message},
           {"role": "user", "content": f"Context: {context}\n\nQuery: {query_text}"}
       ]
   )
   print("Response:")
   print(completion.choices[0].message.content)
except Exception as e:
   print(f"Error generating response: {e}")

# app = FastAPI()

# client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# @app.get("/")
# def read_root():
#     return {"message": "Hello from FastAPI inside a uv workspace!"}
