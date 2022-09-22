FROM apache/airflow:2.3.0
WORKDIR /
COPY ./requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install -r requirements.txt