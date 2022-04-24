FROM python:3.8

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "comandovermelho.py"]