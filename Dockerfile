# #############################
#
#
# SecuWear Docker Container
#
#
# #############################

# Pull base image
FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


# Set the working dir
RUN mkdir /code
WORKDIR /code

# Copy project
COPY . /code/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt











