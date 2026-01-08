FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Run seed command if enabled
RUN if [ "$RUN_SEED" = "true" ] ; then python manage.py seed_data ; fi

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT --workers 3
