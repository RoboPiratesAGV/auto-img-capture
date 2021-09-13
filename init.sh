#! /usr/bin/bash
echo "0" > LAST_SAVED.txt
python3 main.py --url "$1"
