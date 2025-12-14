# Use the latest official Python image (pin for reproducibility if desired)
FROM python:latest
RUN apt-get update && apt-get install -y ffmpeg
# Set working directory
WORKDIR /app

ENV URL=http://localhost:5000

# Install dependencies first to leverage layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

# Set Flask env (optional) and expose port
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

# Recommended: run with gunicorn for production if listed in requirements
# Fallback: `flask run --host=0.0.0.0` if you prefer the dev server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]