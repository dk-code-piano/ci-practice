FROM python:3.15-slim
WORKDIR /app
COPY combo_parser.py main.py ./
ENTRYPOINT ["python", "main.py"]