#!/bin/bash

# start backend index server
python ./peakgptserver.py &
echo "index_server running..."

# wait for the server to start - if creating a brand new huge index, on startup, increase this further
echo "sleeping for 10 seconds to allow index_server to start..."
sleep 10

# start the flask server
echo "starting flask_server..."
python ./peakgptapp.py & echo "flask_server running..."