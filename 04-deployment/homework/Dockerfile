FROM svizor/zoomcamp-model:mlops-3.10.0-slim

RUN pip install -U pip

WORKDIR /app
COPY app /app

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y vim


EXPOSE 8000

CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"]