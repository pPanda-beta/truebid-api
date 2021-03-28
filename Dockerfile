FROM pypy:3.7-slim-buster

RUN pip install --upgrade pip setuptools wheel

WORKDIR /app

ADD ./requirements.txt /app

RUN pip3 install -r /app/requirements.txt

RUN pip3 install gunicorn~=20.1.0

ADD ./ /app

#CMD flask run -h 0.0.0.0 -p ${PORT:-5000}

CMD gunicorn 'app:app' -w 10 -b "0.0.0.0:${PORT:-5000}" --access-logfile -
