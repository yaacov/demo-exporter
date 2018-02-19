FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# set env variables
ENV EXPORTER_PORT="8080" \
    EXPORTER_CONFIG="./openshift-templates/example.yml"

CMD python ./demo-exporter/app.py --config $EXPORTER_CONFIG --port $EXPORTER_PORT
