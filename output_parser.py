from typing import Dict Any
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel Field

class Summary(BaseModel):
    summary: str = Field(description="sumary")
    sentiments: str = Field(description="sentiments")
    
    def to_dict(self) -> Dict[str Any]:
        return {"summary": self.summary, "sentiments": self.sentiments}
        
summary_parser = PydanticOutputParser(pydantic_object=Summary)