from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

role=[SystemMessage(content="You are a Java developer."),
      HumanMessage(content="explain python function")]
print(llm.invoke(role).content)