FROM python:3.9.12


COPY ./requirements.txt /app/
COPY ./simpsons.py /app/

WORKDIR /app/

RUN mkdir General
RUN mkdir Lisa
RUN mkdir Homer 
RUN pip install -r requirements.txt

CMD [ "python3", "simpsons.py" ]


