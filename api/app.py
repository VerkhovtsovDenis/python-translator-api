from fastapi import FastAPI
from Translator import Translator
from constants import SupportLanguages
from .schemas import TranslateInput, TranslateOutput

app = FastAPI(
    title="PascalTranslate API",
    description=(
        "PascalTranslate API — это FastAPI приложение для трансляции "
        "pascal в другие языки программирования."
    ),
)


@app.post("/translate")
async def translate(translate_data: TranslateInput) -> TranslateOutput:
    try:
        result_code = Translator.pascla_translate(
            translate_data.pascal_code, translate_data.target_language
        )
        return TranslateOutput(result_code=result_code, erors="")
    except Exception as e:
        return TranslateOutput(result_code="", erors=str(e))
