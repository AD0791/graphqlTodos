# Use the official Python base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /server

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the app files into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 8000

# Start the app with Uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
