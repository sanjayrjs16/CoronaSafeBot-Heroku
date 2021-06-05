### This script is triggered from within docker contrainer
### to start multiple processes in the same container.
### This script is defined in the CMD option in Dockerfile

# Start actions server in background
cd actions&
rasa run actions --actions actions&

# Start rasa server with nlu model
rasa run --model /app/models --enable-api \
        --endpoints /app/config/endpoints.yml \
        --credentials /app/config/credentials.yml
