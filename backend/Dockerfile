FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp

RUN apk add --no-cache --virtual .build-deps \
            gcc \
            libc-dev \
            linux-headers \
            curl-dev \
        && apk add --no-cache --virtual .python-deps \
            postgresql-dev \
        && pip install --no-cache-dir -r /tmp/requirements.txt \
        && find /usr/local \
            \( -type d -a -name test -o -name tests \) \
            -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
            -exec rm -rf '{}' + \
        && runDeps="$( \
            scanelf --needed --nobanner --recursive /usr/local \
                    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                    | sort -u \
                    | xargs -r apk info --installed \
                    | sort -u \
            )" \
        && apk add --no-cache --virtual .run-deps $runDeps \
        && rm /tmp/requirements.txt \
        && apk del .build-deps

COPY ./src /src

WORKDIR /src

COPY configs/uwsgi.ini .

EXPOSE 8000