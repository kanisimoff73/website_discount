FROM python:3.11-slim


WORKDIR /app
COPY . /app/
RUN apt-get update && apt-get install -y curl && apt-get clean
RUN pip install -r requirements.txt

CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='doot').exists() or User.objects.create_superuser('doot', 'doot@example.com', 'doot')" \
    && python manage.py activate_parser \
    && python manage.py collectstatic --noinput\
    && gunicorn website.wsgi:application --bind 0.0.0.0:8000