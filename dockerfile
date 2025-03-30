FROM python:3.10.12-alpine

WORKDIR /translator_app

COPY requirements.txt /translator_app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /translator_app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]