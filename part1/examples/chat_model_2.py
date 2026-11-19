from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()  # Load environment variables from .env file
llm=ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
response=llm.invoke("Write a poem about a lonely computer.")
# print(response)
# print("================")
# print("type:", type(response))
# print("content:", response.content)
usage=response.usage_metadata
if usage:
    print("Input Tokens:", usage['input_tokens'])
    print("Output Tokens:", usage['output_tokens'])
    print("Total Tokens:", usage['total_tokens'])