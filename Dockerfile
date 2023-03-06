FROM python:3.9-alpine
ADD . /talana_fight
WORKDIR /talana_fight

CMD [ "python", "main.py"]