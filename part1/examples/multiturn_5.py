from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage,HumanMessage, SystemMessage

load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
history=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="explain Quantum Computing in brief."),
]
response=llm.invoke(history)
print("first turn around:", response.content)
history.append(AIMessage(content=response.content))
history.append(HumanMessage(content="explain in a specialist manner"))
response2=llm.invoke(history)
print("second turn around:", response2.content)
history.append(AIMessage(content=response2.content))
history.append(HumanMessage(content="what is the level of Quantum Computing in 2024?"))
response3=llm.invoke(history)
print("third turn around:", response3.content)