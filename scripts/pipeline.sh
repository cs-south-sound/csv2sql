#!/bin/bash

# Check if virtual environment exists

# Activate virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt

cd scripts

# Run python script
python3 load.py

cd ..

# Deactivate virtual environment
deactivate