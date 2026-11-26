from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.language_models import LanguageModelInput

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)
questions:list[LanguageModelInput]=[
   [HumanMessage(content="structure of ChatPromptTemplate?")],
   [HumanMessage(content="structure of response of ChatPromtTemplate?")],
   [HumanMessage(content="Structure of PromptTemplate?")],
 ]
response=llm.batch(questions,config={"max_concurrency": 3})
for k in response:
   print(k.content)
