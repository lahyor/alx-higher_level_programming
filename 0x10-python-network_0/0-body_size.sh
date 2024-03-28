#!/bin/bash
# Send a request to URL and display the sizes in bytes
curl -s "$1" | wc -c
