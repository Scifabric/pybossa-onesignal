# PYBOSSA OneSignal library
[![Build Status](https://travis-ci.org/Scifabric/pybossa-onesignal.svg?branch=master)](https://travis-ci.org/Scifabric/pybossa-onesignal) [![Coverage Status](https://coveralls.io/repos/github/Scifabric/pybossa-onesignal/badge.svg?branch=master)](https://coveralls.io/github/Scifabric/pybossa-onesignal?branch=master) [![Code Health](https://landscape.io/github/Scifabric/pybossa-onesignal/master/landscape.svg?style=flat)](https://landscape.io/github/Scifabric/pybossa-onesignal/master)

## Intro

This is a tiny library that allows you to send push messages using the OneSignal.com service.

The library is really simple, you pass it the app_id (or list of app_ids) and the API key, and 
you are done! 

```python
from pbsonesignal import PybossaOneSignal

client = PybossaOneSignal(api_key="yourkey", app_id="ID")

client.push_msg(contents={"en": "Your message in English", "es": "Tu mensaje en Español"})
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

## Exceptions

If you build the wrong push message, you will get in the console and also an exception with information about it.

## Copyright / License
Copyright 2017 SciFabric LTD.

Source Code License: The GNU Affero General Public License, either version 3 of the License or (at your option) any later version. (see COPYING file)

The GNU Affero General Public License is a free, copyleft license for software and other kinds of works, specifically designed to ensure cooperation with the community in the case of network server software.

Documentation and media is under a Creative Commons Attribution License version 3.
