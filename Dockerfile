# Use a slim version of Python
FROM python:3.11-slim


# Set the working directory in the Docker image
WORKDIR /app


RUN pip install 'uvicorn[standard]'
RUN pip install gunicorn
COPY requirements.txt .
# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of application's source code
COPY . .


# CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app:app"]
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]
CMD uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}
