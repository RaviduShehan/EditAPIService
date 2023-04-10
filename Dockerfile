FROM python:buster
WORKDIR /EditApp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
EXPOSE 5003
ENTRYPOINT ["python", "./src/editService.py"]