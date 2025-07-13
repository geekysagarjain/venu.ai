import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers.string import StrOutputParser
from third_party.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from dotenv import load_dotenv

#information=scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/mrsagarjain/", mock=True)

def ice_break_with(name: str)->str:
    linkedin_username=linkedin_lookup_agent(name=name)
    lindedin_data=scrape_linkedin_profile(linkedin_profile_url=linkedin_username)
    summary_template = """ give the Linkedin information about {person} person form I want you to create: 
    1) A short summary
    2) Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")  #This is for OpenAI model
    #llm = ChatOllama(model="llama3") #This is for llama3 model
    #llm = ChatOllama(model="mistral")

    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"person": lindedin_data})
    print(res)


if __name__ == '__main__':
    load_dotenv()
        
    print('Scraping Data Of A User')

    ice_break_with("mrsagarjain")


    