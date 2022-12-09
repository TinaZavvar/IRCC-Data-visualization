# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10.8-slim

RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
ENV PYTHONBUFFERED 1

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1
RUN mkdir /djangoprjt

WORKDIR /djangoprjt
# Install pip requirements
RUN pip freeze > requirements.txt
RUN pip install --upgrade pip
COPY requirements.txt /djangoprjt/
RUN pip install -r requirements.txt



COPY . /djangoprjt/
EXPOSE 8000
# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python3-debug
# File wsgi.py was not found. Please enter the Python path to wsgi file.
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# # For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python:3.9-slim

# EXPOSE 8000

# # Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# RUN mkdir /app

# # Install pip requirements
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt

# WORKDIR /app
# COPY . /app



# # Creates a non-root user with an explicit UID and adds permission to access the /app folder
# # For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# # RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# # USER appuser

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# # CMD ["gunicorn", "--bind", "0.0.0.0:8000", "irccDataVisualizationSystem.wsgi"]
