# 1 
FROM python:3.7

# 2
COPY src/ /app
WORKDIR /app

# 3
RUN pip install -r requirements.txt

# 4
ENV PORT 8080

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:appx