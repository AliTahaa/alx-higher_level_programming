#!/bin/bash
# takes in a URL displays the body of the response
curl -sX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD" -L
