import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.agents import(create_react_agent, AgentExecutor)
from langchain import hub
from tools.tavily import get_profile_url_tavily


load_dotenv()

def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    
    summary_template=""" Given the full name {name_of_the_person}, return only the URL to their LinkedIn profile. Do not include any text other than the URL. """

    prompt_template = PromptTemplate(input_variables=["name_of_the_person"], template=summary_template)

    tool_for_agent=[
        Tool(
            name="Crawl 4 linkedin profile pages from google",
            func=get_profile_url_tavily,
            description="useful when you need linkedin profile page URL"
        )
    ]

    react_prompt=hub.pull("hwchase17/react")

    agent=create_react_agent(llm=llm, tools=tool_for_agent, prompt=react_prompt)
    agent_executor=AgentExecutor(agent=agent, tools=tool_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input" : prompt_template.format_prompt(name_of_the_person=name)})
    

    linkedin_profile_url=result["output"]

    return linkedin_profile_url

if __name__ == '__main__':
    linkedin_url=lookup(name="mrsagarjain")

    print(linkedin_url)