from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)
chat_tmpl=ChatPromptTemplate.from_messages([
   ("system","You a {domain} expert"),
   ("human","summarize {count} of {contents}"),
])

for domain,contents,n in [
   ("health","daycare",4),
   ("public health","types of patients",3)

]:
   messages=chat_tmpl.format_messages(
      domain=domain,
      contents=contents,
      count=n
   )
   response=llm.invoke(messages)
   print(f"[{contents}]\n{response.content}\n")
