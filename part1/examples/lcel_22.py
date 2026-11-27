from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
tmpl=ChatPromptTemplate.from_template("explain how {topic} works and create png image with description")
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)

# messages=tmpl.format_messages(topic="spring security")
# response=llm.invoke(messages)
# print(response.content)

print("=========")

#LCEL
chain=tmpl|llm
result=chain.invoke({"topic":"spring security"})
print(result.content)
