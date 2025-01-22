import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()
    print("Hello Langchain")

    summary_template = """
        from the given linked in profile information {information} about a person I want you to create:
        1. short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"],template= summary_template)
    # llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3")
    chain = summary_prompt_template | llm | StrOutputParser()

    linkedin_data = scrape_linkedin_profile(
            linkedin_profile_url="www.linkedin.com/in/kaushal-patankar-28ba604/",mock=True
    )

    res = chain.invoke(input={"information":linkedin_data});

    print(res)



