from fastapi import FastAPI
from Translator import Translator
from .schemas import TranslateInput, TranslateOutput


app = FastAPI(
    title="PascalTranslate API",
    description=(
        "PascalTranslate API — это FastAPI приложение для трансляции "
        "pascal в другие языки программирования."
    ),
    openapi_prefix="/translator-api",
)


@app.post("/translate")
async def translate(translate_data: TranslateInput) -> TranslateOutput:
    try:
        result_code = Translator.pascla_translate(
            translate_data.pascal_code, translate_data.target_language
        )
        return TranslateOutput(result_code=result_code, errors="")
    except Exception as e:
        return TranslateOutput(result_code="", errors=str(e))
