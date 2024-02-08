FROM python:3.10-slim

WORKDIR /code

RUN apt-get update \
 && apt-get install tdsodbc -y \
 && apt-get install iputils-ping -y \
 && apt-get install --reinstall build-essential -y

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

EXPOSE 83

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "83", "--reload"]