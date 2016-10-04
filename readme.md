# DontHateMeBot: Twitter Mention Service
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/mkorkmaz/DontHateMeBot/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/mkorkmaz/DontHateMeBot/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/mkorkmaz/DontHateMeBot/badges/build.png?b=master)](https://scrutinizer-ci.com/g/mkorkmaz/DontHateMeBot/build-status/master)


A simple Twitter Mention Service script written in Python.

###Tags
\#python, #python3, #twiter, #streamingapi, #firehose #bot

### Installation
Install the latest versions of required packages
```
$ pip3 install -r pip.install
```
Don't forget to create a new twitter app at (https://apps.twitter.com/) If you haven't yet.

You will need Twitter api_key, api_secret, access_token and access_token_secret.
You can find and/or create them at "Keys and Access Tokens" tab of your Twitter app details page.

### Configuration
Copy config.sample.ini to same folder with firehose.py as config.ini and change variables.

This script uses Twitter's Firehose API. One Firehose service can serve for up to [400 keywords](https://dev.twitter.com/streaming/reference/post/statuses/filter).
But I don't recommend to use more than 9-10 keywords.
If you chose a common keyword as a filter, use one dedicated service for it.

For each keywords in congif.ini, add responses respectively.

### Server Configuration Recommendation
I personally use mostly Ubuntu Server.
For the Firehose service I recommend you to use any VPS server has 1 CPU and 512MB RAM or 1 CPU and 1GB RAM.
Since this service does not support multi-threading more than 2 CPU core would be useless.

Twitter allows one Firehose connection per IP address. This means you can use only one Firehose service for one server. [CitationNeeded].

Use more than one servers has small resources than one server has more resources if you need.

Read more details on Twitter's Streaming Documentation's [connection page](https://dev.twitter.com/streaming/overview/connecting).

### Usage

```
$ python3 ./firehose.py
```

### Ubuntu Upstart Service

Create a configuration file at **/etc/init/tw_firehose.conf** with following contents. Change the file path according to your setup.

```
description "DontHateMeBot"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
setuid nobody
setgid nogroup

exec python3 /home/userhome/firehose.py
```

**Service management**

```
sudo service tw_firehose start|stop|restart
```

### Ubuntu Systemd Service

Create a configuration file at **/etc/systemd/system/firehose.service** with following contents. Change the file path according to your setup.

```
[Unit]
Description=DontHateMeBot

[Service]
ExecStart=/usr/bin/python3 /home/userhome/firehose.py
Restart=always

[Install]
WantedBy=multi-user.target
```

**Service management**

```
sudo systemctl start|stop|restart firehose 
```

### Disclaimer
Don't use this script to abuse random people on the internet. 
I do not accept any responsibility or liability if someone abuses people on the internet using this script