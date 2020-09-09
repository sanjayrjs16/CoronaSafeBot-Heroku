FROM rasa/rasa:latest

COPY . /app

WORKDIR /app

RUN  rasa train

WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

RUN apt-get update rm -rf /var/lib/apt/lists/* &&\
    apt-get -y install gcc --no-install-recommends &&\
    pip3 install -r requirements-actions.txt
# Install extra requirements for actions code, if necessary (uncomment next line)

WORKDIR /app

# By best practices, don't run the code with root user

RUN chmod -R 777 /app/scripts/*

ENTRYPOINT []

CMD  bash /app/scripts/start_services.sh
