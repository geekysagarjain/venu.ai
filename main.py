import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


if __name__=='__main__':
    print('hello langchain')
    print(os.environ['OPENAI_API_KEY'])