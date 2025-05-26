# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

ARG BASE_URL
ARG USER_EMAIL
ARG USER_PASSWORD

ENV BASE_URL=$BASE_URL
ENV USER_EMAIL=$USER_EMAIL
ENV USER_PASSWORD=$USER_PASSWORD


# Install any needed packages specified in requirements.txt
RUN  pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt

# Copy any necessary configurations, such as Allure or environment configs

# Default command to run your tests
CMD ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "allure-results"]
