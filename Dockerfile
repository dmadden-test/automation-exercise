# Use an official Python runtime as a parent image
FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install Java which is needed for allure to run
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jdk \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN curl --insecure -o allure.zip -L "https://github.com/allure-framework/allure2/releases/download/2.34.0/allure-2.34.0.zip" \
    && unzip allure.zip -d /opt/ \
    && mv /opt/allure-2.34.0 /opt/allure \
    && ln -s /opt/allure/bin/allure /usr/bin/allure \
    && rm allure.zip

RUN java --version && allure --version && python --version

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN  pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt

# Default command to run your tests
CMD ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "allure-results"]
