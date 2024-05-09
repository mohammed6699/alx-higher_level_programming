#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the respose

if [ $# -ne 1 ]; then
	exit 1
fi

url="0.0.0.0:5000"
response=$(curl -s -o - "$url")
size=$(echo "$response" | wc -c )
echo "$size"
