FROM rasa/rasa-sdk:1.9.0


# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
COPY requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

RUN apt-get update rm-rf/var/lib/apt/lists/* &&\
    apt-get -y install gcc --no-install-recommends &&\
    pip3 install -r requirements-actions.txt
# Install extra requirements for actions code, if necessary (uncomment next line)

WORKDIR /app

# Copy actions folder to working directory
COPY ./ /app/actions

# By best practices, don't run the code with root user


ENTRYPOINT []

CMD python3 -m rasa-sdk --actions actions -p $PORT

USER 1001
