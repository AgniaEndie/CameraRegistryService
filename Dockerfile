FROM python:3.12-slim
LABEL authors="agniaendie"

COPY src /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
ENTRYPOINT ["python","CameraRegistryService.py"]