#!/bin/bash
# breaking to http protocols on school servers
curl -s -L -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me
