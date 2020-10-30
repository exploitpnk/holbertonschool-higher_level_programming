#!/bin/bash
# displays the body of the response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
