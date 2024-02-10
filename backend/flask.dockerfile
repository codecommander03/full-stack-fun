FROM python:3.6-slim-buster

# Set the working directory
WORKDIR /app

COPY requirements.txt ./

# Install the requirements
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

EXPOSE 4000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]