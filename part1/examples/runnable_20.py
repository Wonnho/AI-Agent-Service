from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
prompt=ChatPromptTemplate.from_template("explain {topic} in one sentence")
model=ChatOpenAI(model="gpt-4o-mini",temperature=0)
print(hasattr(prompt,"invoke"))
print(hasattr(model,"invoke"))
print("==========")
chain=prompt|model
print(hasattr(chain,"invoke"))
print(hasattr(chain,"stream"))
print(hasattr(chain,"batch"))
print("==========")
result=chain.invoke({"topic":"Template Object"})
print(result.content)