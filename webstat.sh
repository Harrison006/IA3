#!/bin/bash

python3 ./python/api/stats.py &
python3 ./python/api/asses.py &
python3 -m http.server &