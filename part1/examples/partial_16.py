from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)
summary_tmpl=ChatPromptTemplate.from_messages(
   [
       ("system","you an API expert"),
               ("human","summarize {text} API design in short in {language}")
   ]
)
print(summary_tmpl.input_variables)

summary_ko=summary_tmpl.partial(language="korean")
print(summary_ko.input_variables)
messages=summary_ko.format_messages(
   text="Langchain is a python framework helping LLM application "
)

response=llm.invoke(messages)
print(response.content)