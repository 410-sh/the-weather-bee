#!/bin/bash

#download waitress
pip install waitress-serve

#create working diectory
DIR="/home/ubuntu/the-weather-bee"
if [ -d "$DIR" ]; then
	echo "${DIR} exists"
else
	echo "Creating {$DIR} directory"
	mkdir ${DIR}
fi
