from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()  # Load environment variables from .env file
llm=ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
messages=[
    SystemMessage(
      content=("You are a senior backend developer."
                  "explain in a specialist manner, and provide code examples in Java.")
                  ),
    HumanMessage(
      content="what is UserDetailsService in Spring Boot?"),
]
response=llm.invoke(messages)
print("collaborative level response:", response.content)
