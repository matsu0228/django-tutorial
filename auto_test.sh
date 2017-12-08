#!/bin/bash

source ./myvenv/bin/activate
result=$(python manage.py test 2>&1 1>/dev/null | tail -n 1)
echo -e "
result:
${result}"