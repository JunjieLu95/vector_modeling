FROM python:3.12-slim
WORKDIR /app
COPY setup.py .
COPY README.md .
COPY src/ src/
COPY tests/ tests/
RUN pip install --upgrade pip && pip install . && pip install pytest
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]
