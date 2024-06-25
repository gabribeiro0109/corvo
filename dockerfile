FROM python
Desafio Pipeline, rodar arquivo de RPA Dolar: 4
WORKDIR /app
COPY rpa.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "rpa.py" ]
