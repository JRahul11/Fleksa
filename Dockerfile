# Get Image for Python 3.7
FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt

# Install requirements
RUN pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app

ADD . .

# Create Tables
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic

# For Local Deployment
# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "fleksa.wsgi:application"]

# For Hosting
CMD gunicorn fleksa.wsgi:application --bind 0.0.0.0:$PORT