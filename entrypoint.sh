#!/bin/bash

black .

pip freeze > requirements.txt

export PYTHONPATH=/Users/shaxzodbek/Developer/bot_structure


python app/server/server.py


