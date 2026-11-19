from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage,HumanMessage, SystemMessage

load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

response=HumanMessage(content="remember my name is Musk")
print("first turn around:", response.content)
response2=llm.invoke("what is my name?")
print("second turn around:", response2.content)