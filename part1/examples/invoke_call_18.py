from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)
messages=[
   ("system","You a programming expert"),
   ("human","summarize SOLID of Java"),
]
response=llm.invoke(messages)
print("content",response.content)