FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel

RUN useradd -m -u 1000 user

WORKDIR /app

COPY --chown=user ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=user . /app

RUN python3 download_model_flan.py

ENV DEFAULT_STATEMENT="Lilypad is awesome"

ENTRYPOINT ["python3", "inference.py"]

ENV STATEMENT="${DEFAULT_STATEMENT}"