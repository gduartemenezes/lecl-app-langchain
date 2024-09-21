from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi")
]

model = ChatOpenAI(model="gpt-4")

result = model.invoke(messages)
parser.invoke(result)

print(parser.invoke(result))


