# PYBOSSA OneSignal library
[![Build Status](https://travis-ci.org/Scifabric/pybossa-onesignal.svg?branch=master)](https://travis-ci.org/Scifabric/pybossa-onesignal) [![Coverage Status](https://coveralls.io/repos/github/Scifabric/pybossa-onesignal/badge.svg?branch=master)](https://coveralls.io/github/Scifabric/pybossa-onesignal?branch=master) [![Code Health](https://landscape.io/github/Scifabric/pybossa-onesignal/master/landscape.svg?style=flat)](https://landscape.io/github/Scifabric/pybossa-onesignal/master)
[![Python 2.7](https://img.shields.io/badge/python-2.7-green.svg)](https://pypi.python.org/pypi/pybossa-onesignal/)
[![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://pypi.python.org/pypi/pybossa-onesignal/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-orange.svg)](https://pypi.python.org/pypi/pybossa-onesignal/)

## Intro

This is a tiny library that allows you to send push messages using the OneSignal.com service.

The library is really simple, you pass it the app_id (or list of app_ids) and the API key, and 
you are done! 

```python
from pbsonesignal import PybossaOneSignal

client = PybossaOneSignal(api_key="yourkey", app_id="ID")

client.push_msg(contents={"en": "Your message in English", "es": "Tu mensaje en Español"})
```


In the case that you want to create a new app, just do the following:

```python
from pbsonesignal import PybossaOneSignal

client = PybossaOneSignal(auth_key="yourkey")

client.create_app('name', 'https://yoursite.com', 'https://yoursite.com/icon')
```


## Arguments for push_msg

The following is a list of all the arguments you can use with this client:

### contents

This is a dictionary that allows you send a message in different languages:

```python
contents = {"en": "Your message in English", "es": "Tu mensaje en Español"}
```

Add as many languages as you want.

### headings

This is a dictionary that allows you send a heading in different languages:

```python
headings = {"en": "Your heading in English", "es": "Tu título en Español"}
```

Add as many languages as you want.

### launch_url

This is a string with the url that should be launched when the user clicks (or touches)
the notification.

```python
url = "http://yoursite.com"
```

### web_buttons

This is an array of dictionaries where you can add buttons to your notifications.

```python
web_buttons=[{"id": "read-more-button",
              "text": "Read more",
              "icon": "http://i.imgur.com/MIxJp1L.png",
              "url": "https://yoursite.com"}],
```
### chrome_web_image

This is a string with the full URL to an image that you want to show in the body of the notification.

```python
chrome_web_image="https://yourimage.com",
```

### chrome_web_icon

This is a string with the full URL to an icon that you want to show in the notification.

```python
chrome_web_icon="https://yourimage.com",
```

### included_segments

This is a list of string. It lists all the segments you will be sending the notification. By default is All.

```python
included_segments=["All"],
```

### excluded_sements 

This is a list of string. It lists all the segments you will *not* be sending the notification. By default is empty.

```python
excluded_sements=[],
```

### filters

This is a list of dictionaries. It allows you to filter your segments. By default is empty.

```python
filters=[],
```
### include_player_ids

This is a list of strings. Specify player IDs to only send the notifications to them. By default is None, so it will be sent to all the users.

```python
include_player_ids=None
```

### send_after

This is a string. Specify a date and time to send the notification. By default is None, so it will be sent immediately.

```python
send_after=None
```

### delayed_option

This is a string. Specify when it has be delayed. By default is None.

```python
delayed_option=None
```

### delivery_time_of_day

This is a string. Specify the time when it will be sent. By default is None.

```python
delivery_time_of_day=None
```

### ttl

This is a string. Specify the time to live of the notification below deleting it for the user. By default is 3 days.

```python
ttl=None
```

### priority

This is a string. Specify the priority. By default is normal. Use 10 to make it higher.

```python
priority=None

## create_app

You can also create an app in OneSignal.com. Just run the following:

**NOTE**: You need to start the client with your auth_key. Without that you will not
be able to create apps.
```
```python
from pbsonesignal import PybossaOneSignal

client = PybossaOneSignal(api_key="yourkey", app_id="ID", auth_key="yourkey")

client.create_app('name_app', 'https://yourdoamin.com', 'https://yourdomain/icon.png')
```


## Arguments for create_app

You can use the following arguments for this method.

### name

This is a string. The name of the app you will be creating in OneSignal.

```python
name='yourappname'
```

### chrome_web_origin

This is a string. The URL of the site that you will be linking to the app.

```python
chrome_web_origin='https://yoursite.com'
```

**WARNING**: Read their docs, but you need **full HTTPS in your site** so this can work.

### chrome_web_default_notification_icon

This is a string. The URL of the default notification icon

```python
chrome_web_default_notification_icon='https://yoursite.com/assets/img/icon.png'
```

**WARNING**: Read their docs, but you need **full HTTPS in your site** so this can work.


## Exceptions

If you build the wrong push message or you create the wrong app, you will get in the console and also an exception with information about it.

## Copyright / License
Copyright 2017 Scifabric LTD.

Source Code License: The GNU Affero General Public License, either version 3 of the License or (at your option) any later version. (see COPYING file)

The GNU Affero General Public License is a free, copyleft license for software and other kinds of works, specifically designed to ensure cooperation with the community in the case of network server software.

Documentation and media is under a Creative Commons Attribution License version 3.
