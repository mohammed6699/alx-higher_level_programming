#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

if [ $# -ne 1 ];then
	exit 1
fi

response=$(curl -sL -X DELETE "$1")
echo "I'm a DELETE request"
