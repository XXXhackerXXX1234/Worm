#!/bin/bash
# This script will automatically run a Python script

# Path to your Python script
PYTHON_SCRIPT="./main.py"

# Number of times to run the script
RUN_COUNT=100

# Check if the Python script exists
if [ -f "$PYTHON_SCRIPT" ]; then
    for i in $(seq 1 $RUN_COUNT); do
        echo "Running $PYTHON_SCRIPT (iteration $i)..."
        python3 "$PYTHON_SCRIPT"
    done
else
    echo "Error: $PYTHON_SCRIPT does not exist."
    exit 1
fi
