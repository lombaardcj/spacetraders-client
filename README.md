# spacetrade

Go to getting started - https://docs.spacetraders.io/

Register an agent :
```
curl --request POST \
 --url 'https://api.spacetraders.io/v2/register' \
 --header 'Content-Type: application/json' \
 --data '{
    "symbol": "INSERT_CALLSIGN_HERE",
    "faction": "COSMIC"
   }'
```

# STORE YOUR TOKEN for you callsign into `.env` file by updating `TOKEN=`

Enjoy!
