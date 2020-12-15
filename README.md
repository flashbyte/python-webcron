# python-webcron

A small webcron app in a alpine docker container writen in python.
It is intended to be used to trigger nextcloud cron jobs, but can be use for any webservice triggering.

## Run Docker
```
docker run --name "webcron" -e TIME="300" -e URL="http://my-nextcloud.example.com/cron.php" flashbyte/python-webcron
```

## Parameters

### URL:
The URL to be triggered
Default: http://app/cron.php

### TIME:
Time in seconds to wait in between
Default: 300s

### Debug:
More debuging infos. true/false
Default: false