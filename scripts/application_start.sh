#!/bin/bash

#give permission for everything in the express-app directory
sudo chmod -R 777 /home/ubuntu/the-weather-bee

#navigate into our working directory where we have all our github files
cd /home/ubuntu/the-weather-bee

#add run waitress-serve to host the app
sudo waitress-serve --port=80 main:app
