FROM python:3.7

COPY . /web
WORKDIR /web
RUN pip install -r ./requirements.txt


CMD ["python", "-m", "unittest", "discover", "-s","Tests"]