#!/bin/bash

python wbs.py &>/dev/null

sed s/KEYWORD/$1/ query.js|mongo
