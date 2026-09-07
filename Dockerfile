# 1. Use an official lightweight Python runtime as a parent image
FROM python:3.12-slim

# 2. Set environment variables to optimize Python for Docker
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Create a non-root user and group for security
RUN groupadd -r appgroup && useradd -r -g appgroup -d /app -s /sbin/nologin appuser

# 5. Copy dependencies specification first to leverage Docker layer caching
COPY requirements.txt .

# 6. Install Python dependencies without storing pip cache
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copy application source code into the container
COPY app/ ./app

# 8. Set correct file ownership for the non-root user
RUN chown -R appuser:appgroup /app

# 9. Switch to the non-root user
USER appuser

# 10. Expose port 8000 for documentation and network mapping
EXPOSE 8000

# 11. Define the default command to run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
