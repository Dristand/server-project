FROM python:3

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN useradd guest
USER guest
CMD [ "python" ,"main.py" ]