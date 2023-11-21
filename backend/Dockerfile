FROM python:3.11.5-alpine3.18

COPY ./backend/requirements.txt /requirements.txt
COPY ./backend /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
WORKDIR /app/app
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
