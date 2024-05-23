ARG BASE_REGISTRY=registry1.dso.mil
ARG BASE_IMAGE=ironbank/opensource/python
ARG BASE_TAG=v3.10.11

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

USER root

COPY requirements.txt .
COPY \
  __init__.py \
  main.py \
  schemas.py \
  /home/python/


RUN python -m pip install pip --upgrade
RUN python -m pip install --no-cache-dir -r requirements.txt

USER python
WORKDIR /home/python/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000
