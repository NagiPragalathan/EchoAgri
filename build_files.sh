#!/bin/bash

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Run Django collectstatic command
python3.9 manage.py collectstatic --noinput