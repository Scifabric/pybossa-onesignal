# -*- coding: utf8 -*-
# This file is part of PYBOSSA.
#
# Copyright (C) 2017 Scifabric LTD.
#
# PYBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PYBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PYBOSSA.  If not, see <http://www.gnu.org/licenses/>.
"""
PYBOSSA module for sending Web PUSH notifications.

This module exports:
    * OneSignal Class: to create apps and send notifications.

"""
import requests
from exceptions import *


class PybossaOneSignal(object):

    """General class for PybossaOneSignal."""

    api_url = 'https://onesignal.com/api/v1/notifications'
    api_apps = 'https://onesignal.com/api/v1/apps'

    def __init__(self, api_key=None, app_id=None, app_ids=None, auth_key=None):
        """Initiate."""
        try:
            if api_key is None and auth_key is None:
                msg = "Provide some credentials API key or AUTH key."
                raise ApiAuthKeysMissing
            self.api_key = api_key
            self.auth_key = auth_key
            self.app_id = app_id
            self.app_ids = app_ids
            if app_id and app_ids:
                msg = "You can only provide or an app_id or a list of app_ids"
                raise AppIdDuplicate(msg)
            if app_id:
                self.app_ids = [app_id]
            else:
                self.app_ids = app_ids
        except Exception as e:
            print "ERROR: %s: %s" % (type(e), e)
            raise e

    def header(self, auth):
        """Return proper Header for authenticating."""
        return {"Content-Type": "application/json; charset=utf-8",
                "Authorization": "Basic %s" % auth}

    def push_msg(self, contents={"en": "English Message"},
                 headings={"en": "Heading"},
                 launch_url="https://yoursite.com/",
                 web_buttons=[{"id": "read-more-button",
                               "text": "Read more",
                               "icon": "http://i.imgur.com/MIxJp1L.png",
                               "url": "https://yoursite.com"}],
                 chrome_web_image="https://yourimage.com",
                 chrome_web_icon="https://image",
                 included_segments=["All"],
                 excluded_sements=[],
                 filters=[],
                 include_player_ids=[],
                 send_after=None,
                 delayed_option=None,
                 delivery_time_of_day=None,
                 ttl=None,
                 priority=None):
        """Push notification message."""

        try:
            if self.api_key is None:
                msg = "API key is missing"
                raise ApiKeyMissing(msg)

            if self.app_id is None and self.app_ids is None:
                msg = "You should provide an app_id or an array of app_ids"
                raise AppIdMissing(msg)

            payload = {
                       "included_segments": included_segments,
                       "excluded_sements": excluded_sements,
                       "filters": filters,
                       "contents": contents,
                       "headings": headings,
                       "url": launch_url,
                       "web_buttons": web_buttons,
                       "chrome_web_image": chrome_web_image,
                       "chrome_web_icon": chrome_web_icon}

            if len(self.app_ids) == 1:
                payload['app_id'] = self.app_ids[0]
            else:
                payload['app_ids'] = self.app_ids

            if len(include_player_ids) > 0:
                payload['include_player_ids'] = include_player_ids

            if send_after:
                payload['send_after'] = send_after

            if delayed_option:
                payload['delayed_option'] = delayed_option

            if delivery_time_of_day:
                payload['delivery_time_of_day'] = delivery_time_of_day

            if ttl:
                payload['ttl'] = ttl

            if priority:
                payload['priority'] = priority

            headers = self.header(self.api_key)

            req = requests.post(self.api_url,
                                headers=headers,
                                json=payload)

            response = req.json()

            if 'errors' in response.keys():
                for error in response['errors']:
                    raise CreateNotification(error)
            return (req.status_code, req.reason, req.json())
        except CreateNotification as e:
            print "ERROR: %s: %s" % (type(e), e)
            raise e

    def create_app(self, name,
                   chrome_web_origin,
                   chrome_web_default_notification_icon,
                   **kwargs):
        """Create a OneSignal app."""
        try:
            if self.auth_key is None:
                msg = "Auth key missing."
                raise AuthKeyMissing(msg)

            payload = dict(name=name,
                           chrome_web_origin=chrome_web_origin,
                           chrome_web_default_notification_icon=chrome_web_default_notification_icon,
                           )

            payload.update(kwargs)

            headers = self.header(self.auth_key)

            req = requests.post(self.api_apps,
                                headers=headers,
                                json=payload)

            response = req.json()

            if 'errors' in response.keys():
                for error in response['errors']:
                    raise CreateApp(error)
            return (req.status_code, req.reason, req.json())
        except CreateApp as e:
            print "ERROR: %s: %s" % (type(e), e)
            raise e

