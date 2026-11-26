from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)
messages=[
   ("system","You a programming expert"),
   ("human","summarize interface of Java"),
]

for chunk in llm.stream(messages):
   print(chunk.content,end="",flush=True)
print()