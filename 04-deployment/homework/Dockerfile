FROM svizor/zoomcamp-model:mlops-3.10.0-slim

RUN pip install -U pip

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y vim

COPY src /app

EXPOSE 8000

CMD ["uvicorn", "app.predict:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"]