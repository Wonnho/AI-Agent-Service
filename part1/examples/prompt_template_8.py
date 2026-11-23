from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
  "summarize the {count} traits of {object}"
)
prompt1=template.format(object="apple", count=3)
prompt2=template.format(object="analysts forecast", count=5)

print('apple:',prompt1)
print('analysts forecast:',prompt2)
