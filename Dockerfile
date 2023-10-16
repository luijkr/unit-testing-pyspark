FROM python:3.12

# Install required dependencies for your project
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk

# Copy your project files into the container
COPY . /

# Install Python requirements
RUN pip install -r requirements.txt

# Run the unit tests by invoking pytest
CMD ["pytest"]
