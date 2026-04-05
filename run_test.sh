#!/bin/bash

# Run pytest using Windows Python
cmd.exe /c "venv\\Scripts\\python.exe -m pytest"
RESULT=$?

if [ $RESULT -eq 0 ]; then
  echo "Tests passed ✅"
  exit 0
else
  echo "Tests failed ❌"
  exit 1
fi