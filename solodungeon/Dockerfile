# Use multi-stage builds to optimize size and caching
# Stage 1: Node.js base for building frontend assets
FROM node:latest as build-stage
WORKDIR /app
COPY solodungeon/frontend/package*.json ./
RUN npm install
COPY solodungeon/frontend/ .
RUN npm run build

# Stage 2: Python base for Django backend
FROM python:3.9-slim
WORKDIR /django
COPY solodungeon/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY solodungeon/backend .

# Copy built static files from build-stage
COPY --from=build-stage /app/build /django/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run the application
CMD ["gunicorn", "solodungeon.wsgi:application", "--bind", "0.0.0.0:8000"]