import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers.string import StrOutputParser
from third_party.linkedin import scrape_linkedin_profile

information=linkedin_profile=scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/mrsagarjain/", mock=True)

if __name__ == '__main__':
    print('hello langchain')
    summary_template = """ give the Linkedin information about {information} person form I want you to create: 
    1) A short summary
    2) Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=[information], template=summary_template)

    #llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")  #This is for OpenAI model
    llm = ChatOllama(model="llama3") #This is for llama3 model

    #llm = ChatOllama(model="mistral")

    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": information})
    print(res)

    