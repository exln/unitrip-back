#!/bin/bash

echo "$ENV"

if [ "$ENV" == "development" ]; then
  alembic upgrade head
fi

python main.py