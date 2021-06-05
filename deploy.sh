#!/bin/bash
hostname=$(curl http://134.209.149.110/metadata/v1/hostname)
docker run -d -p 80:8080 --name coronasafebot-"$hostname" sanjayr16/coronasafebot:"$hostname"
