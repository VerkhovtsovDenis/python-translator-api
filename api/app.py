from fastapi import FastAPI
from Translator import Translator
from constants import SupportLanguages
from .schemas import TranslateInput, TranslateOutput

APP_PREFIX ="translator"

app = FastAPI(
    title="PascalTranslate API",
    description=(
        "PascalTranslate API — это FastAPI приложение для трансляции "
        "pascal в другие языки программирования."
    ),
    docs_url=f"/{APP_PREFIX}/docs",
    openapi_url=f"/{APP_PREFIX}/openapi.json",
)


@app.post(f"/{APP_PREFIX}/translate")
async def translate(translate_data: TranslateInput) -> TranslateOutput:
    try:
        result_code = Translator.pascla_translate(
            translate_data.pascal_code, translate_data.target_language
        )
        return TranslateOutput(result_code=result_code, errors="")
    except Exception as e:
        return TranslateOutput(result_code="", errors=str(e))
