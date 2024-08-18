import os


os.environ["REPLICATE_API_TOKEN"] = "x"

from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.replicate import Replicate
from transformers import AutoTokenizer

# set the LLM
llama2_7b_chat = "meta/llama-2-7b-chat:8e6975e5ed6174911a6ff3d60540dfd4844201974602551e10e9e87ab143d81e"
Settings.llm = Replicate(
    model=llama2_7b_chat,
    temperature=0.01,
    additional_kwargs={"top_p": 1, "max_new_tokens": 300},
)

# set tokenizer to match LLM
Settings.tokenizer = AutoTokenizer.from_pretrained(
    "NousResearch/Llama-2-7b-chat-hf"
)

# set the embed model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(
    documents,
)

query_engine = index.as_query_engine()
result=query_engine.query("List of symptoms for diabetes?")
print(result)
