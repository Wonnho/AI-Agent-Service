from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)
response=llm.invoke(
   ChatPromptTemplate.from_messages(
      [
         ("system","you an API expert"),
         ("human","desing {text} API in {language}")
      ]
   ).format_messages(
      text="요양보험은 4 개의 주체가 관여하고 있다. 환자, 요양보호사, 요양센터, 정부기관",
      language="korean"
   )
)
print(response.content)