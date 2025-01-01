from pydantic import BaseModel
from constants import SupportLanguages


class TranslateInput(BaseModel):
    pascal_code: str
    target_language: SupportLanguages


class TranslateOutput(BaseModel):
    result_code: str
    errors: str
