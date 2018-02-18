FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./demo-exporter/app.py", "--config", "./demo-exporter/example.yml" ]
