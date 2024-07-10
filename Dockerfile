FROM python:3.9.6-slim

RUN useradd -m -u 1000 user

WORKDIR /app

COPY --chown=user ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=user . /app

ENV DEFAULT_STATEMENT="Lilypad is awesome"

ENTRYPOINT ["python3", "inference.py"]

ENV STATEMENT="${DEFAULT_STATEMENT}"