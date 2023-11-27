FROM python

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org Flask

EXPOSE 5000

ENV FLASK_ENV=production

CMD ["python", "app1.py"]
