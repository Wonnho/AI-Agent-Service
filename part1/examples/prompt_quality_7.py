from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

v3=[SystemMessage(content="You are a Java developer."),
      HumanMessage(content="explain java function according to the following rules:"
                   "1.what is the function in Java?"
                   "2.what is the relation of class with it?"
                   "3.what does constructor play in class and why need it?"
                   "target: intermediate level developer"
                   "length: 200 words")]
print(llm.invoke(v3).content)