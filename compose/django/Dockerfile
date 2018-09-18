FROM python:3.6

ENV PYTHONUNBUFFERED 1

ENV ROOTDIR /usr/local/

WORKDIR $ROOTDIR/

ADD ./compose/django/compile.sh $ROOTDIR/src/
ADD ./compose/django/install_extras.sh $ROOTDIR/src/


# Compilation
RUN chmod 777 src/install_extras.sh
RUN src/install_extras.sh

RUN chmod 777 src/compile.sh
RUN src/compile.sh

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements

RUN pip install -r /requirements/production.txt

RUN groupadd -r django && useradd -r -g django django
COPY . /app
RUN chown -R django /app

COPY ./compose/django/gunicorn.sh /gunicorn.sh
COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN sed -i 's/\r//' /gunicorn.sh
RUN chmod +x /entrypoint.sh && chown django /entrypoint.sh
RUN chmod +x /gunicorn.sh && chown django /gunicorn.sh

WORKDIR /app

RUN export DJANGO_SETTINGS_MODULE='config.settings.production';python manage.py compilemessages

ENTRYPOINT ["/entrypoint.sh"]
