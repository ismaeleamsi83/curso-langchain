from pydantic import BaseModel
from typing import List, Optional

# Lo que el usuario nos envía (Input)
class ChatRequest(BaseModel):
    question: str

# Lo que devolvemos (Output)
class ChatResponse(BaseModel):
    answer: str
    # Opcional: listamos las fuentes de donde la IA sacó la información
    sources: Optional[List[dict]] = None