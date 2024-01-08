FROM python:3.8

COPY requirements.txt /myinfoweb/requirements.txt
WORKDIR /myinfoweb
RUN pip install -r requirements.txt

COPY . /myinfoweb

EXPOSE 8800

CMD ["python", "myinfoweb.py"]