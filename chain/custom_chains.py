import os
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
#from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from output_parser import summary_parser

load_dotenv()

def get_summary_chain() -> RunnableSequence:
    summary_template = """
    You are content journalist. Pleae analyze given video transcript {transcript} and user comments {comments}.
    
    Based on your analysis please provide folowing points
    1. A brief summary of video.
    2. User sentiments.
    \n{format_instructions}
    """
    
    api_key = os.getenv("GOOGLE_AI_KEY")
    #llm = ChatOpenAI(temperature=0, model_name="gpt-3.5.turbo")
    llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
    
    summary_prompt_template = PromptTemplate(
        template=summary_template,
        input_variables=["transcript","comments"],
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )
    
    return summary_prompt_template | llm | summary_parser