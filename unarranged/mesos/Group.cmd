@echo off

curl -X POST http://192.168.56.101:8080/v2/apps -d @Group.json -H "Content-type: application/json"

pause