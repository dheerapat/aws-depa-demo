# Use a slim Python 3.9 image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt (if you have one)
COPY requirements.txt .
# Install dependencies (replace with your actual requirements)
RUN pip install -r requirements.txt

# Copy your app source code
COPY . .

# Expose Gradio port (default 7860)
EXPOSE 8000

# Start the Gradio app using command line arguments
CMD ["fastapi", "run", "server.py"]
