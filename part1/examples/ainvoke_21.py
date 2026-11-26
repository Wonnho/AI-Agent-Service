from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage
import asyncio

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)
prompt=ChatPromptTemplate.from_messages(
   [
      ("system","you are a python teacher"),
      ("human","{question}"),
   ]
)

async def ask(question:str):
   messages=prompt.format_messages(question=question)
   result=await llm.ainvoke(messages)
   return result.content

async def main():
   results=await asyncio.gather(
      ask("decorator of python?"),
      ask("generator of python?")
   )
   print(results[0])
   print(results[1])

asyncio.run(main())