FROM python:3.13.2-slim-bullseye

# Install required dependencies for your project
RUN apt-get update && apt-get install -y pip

# Copy your project files into the container
COPY . /

# Install Python requirements
RUN pip install -r requirements.txt

# Run the unit tests by invoking pytest
ENTRYPOINT ["pytest", "."]
