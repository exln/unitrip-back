FROM python:3
ENV PYTHONUNBUFFERED=1
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
ENV PYTHONUNBUFFERED=1
WORKDIR /back/
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /back/
EXPOSE 7878
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7878"]