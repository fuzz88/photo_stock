FROM python:3.10-bullseye

LABEL maintainer="Ivan Oschepkov <ivan@oschepkov.ru>"

COPY requirements.txt /opt/

RUN pip install --no-cache-dir -r /opt/requirements.txt

COPY app/ /opt/app/
COPY entrypoint.sh /opt/

EXPOSE 8081

CMD ["sh", "/opt/entrypoint.sh"]
