FROM rasa/rasa:1.9.6-full

MAINTAINER Sanjay R

WORKDIR /app
COPY . /app
COPY ./data /app/data

RUN  rasa train

ADD ./models /app/models/
ADD ./config /app/config/
ADD ./actions /app/actions/
ADD ./scripts /app/scripts/
ADD ./data /app/data/
ADD ./data/test/lookup_tables/names.txt /app/data/test/lookup_tables
ADD ./data/test/lookup_tables/countries.txt /app/data/test/lookup_tables
ADD ./domain.yml /app/
ADD ./config.yml /app/

WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

RUN apt-get update &&\
    apt-get -y install gcc &&\
    pip3 install -r requirements-actions.txt
# Install extra requirements for actions code, if necessary (uncomment next line)

WORKDIR /app

# Copy actions folder to working directory
COPY ./actions /app/actions

# By best practices, don't run the code with root user

RUN chmod -R 777 /app/scripts/*

ENTRYPOINT []

CMD  bash /app/scripts/start_services.sh

