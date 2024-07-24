from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain.prompt import PromptTemplate
from output_parsers import summary_parser

def get_summary_chain() -> RunnableSequence:
    summary_template = """
    
    """
    
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5.turbo")
    
    summary_prompt_template = PromptTemplate(
        input_variables=["transcript","comments"],
        template=summary_template
        partial_variables={
            "format_istructions": summary_parser.get_forat_instructions()
        }
    )
    
    return summary_prompt_template | llm | summary_parser