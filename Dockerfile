# STEP 1: 
FROM python:3.7-slim-buster

# STEP 2:
RUN pip install Flask
RUN pip install pymongo

# STEP 3:
ADD . /app

# STEP 4:
WORKDIR /app

# STEP 5:
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# STEP 6:
EXPOSE 5000

# STEP 7:
CMD ["flask", "run", "--host=0.0.0.0"]
