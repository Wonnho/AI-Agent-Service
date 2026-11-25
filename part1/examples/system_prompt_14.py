from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)
tmpl=ChatPromptTemplate.from_messages([
   ("system","you are a {role}"),
   ("human","{question}"),
])
question="system design?"
for role in ["Carer","public health"]:
   message=tmpl.format_messages(
      role=role,
      question=question,
   )
   response=llm.invoke(message)
   print(f"[{role}\n{response.content}\n")
