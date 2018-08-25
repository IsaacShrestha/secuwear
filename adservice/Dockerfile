# Pull base image
FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


# Set the working dir
# RUN mkdir /code
WORKDIR /code

# Copy project
COPY . /code/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install django==1.11
RUN pip install djangorestframework
RUN pip install markdown
RUN pip install django-filter==1.1
RUN pip install djangorestframework-jsonapi