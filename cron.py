#!/usr/bin/env python3
import requests
import os
import logging
import time

URL = 'http://app/cron.php'
TIME = '300'
DEBUG = 'false'

logging.basicConfig(level=logging.INFO)

log = logging.getLogger("webcron")

if 'URL' in os.environ:
	URL = os.getenv('URL')
	log.info("--- Set URL to %s ---" %URL)

if 'TIME' in os.environ:
	TIME = os.getenv('TIME')
	log.info("--- Set TIME to %s ---" %TIME)

if 'DEBUG' in os.environ:
	DEBUG = os.getenv('DEBUG')
	log.info("--- Set DEBUG to %s ---" %DEBUG)

if DEBUG == 'true':
	log.setLevel(logging.DEBUG)

while True:
	try:
		r = requests.get(URL)
		log.debug("RESPONS: %s" %r.text)
	except requests.ConnectionError:
		log.error("Could not reach %s" %URL)
	else:
		log.info("%s - Calling %s - %s" %(time.asctime(), URL, r.status_code))


	log.debug("Sleep %s" %TIME)
	time.sleep(int(TIME))

