# -*- coding: utf8 -*-
# This file is part of PYBOSSA.
#
# Copyright (C) 2017 SciFabric LTD.
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
import json
from collections import namedtuple
from pbsonesignal import PybossaOneSignal
from pbsonesignal.exceptions import *
from nose.tools import raises
from mock import patch, MagicMock

FakeRequest = namedtuple('FakeRequest', ['text', 'status_code', 'headers'])


class TestPybossaOnesignal(object):

    valid_notification = {u'id': u'da360e9a-09d9-4992-a803-5bca978c5e0d',
                          u'recipients': 3}

    error_notification = {u'errors': ['an example error']}

    payload = None

    def setUp(self):
        self.payload = {
                        "included_segments": ["All"],
                        "excluded_sements": [],
                        "filters": [],
                        "contents": {"en": "English Message"},
                        "headings": {"en": "Heading"},
                        "url": "https://yoursite.com/",
                        "web_buttons": [{"id": "read-more-button",
                                        "text": "Read more",
                                        "icon": "http://i.imgur.com/MIxJp1L.png",
                                        "url": "https://yoursite.com"}],
                        "chrome_web_image": "https://yourimage.com",
                        "chrome_web_icon": "https://image"}


    @patch('pbsonesignal.requests.post')
    def test_push_msg(self, mock):
        """Test push_msg works."""
        client = PybossaOneSignal(app_id="1", api_key="key")
        fakeRequest = MagicMock()
        fakeRequest.status_code = 200
        fakeRequest.reason = 'OK'
        fakeRequest.json.return_value = self.valid_notification
        mock.return_value = fakeRequest
        tmp = client.push_msg()
        assert tmp[0] == 200
        assert tmp[1] == 'OK'
        assert tmp[2] == self.valid_notification

    @patch('pbsonesignal.requests.post')
    def test_push_msg_app_ids(self, mock):
        """Test push_msg with array app_ids works."""
        client = PybossaOneSignal(app_ids=["1", "2"], api_key="key")
        fakeRequest = MagicMock()
        fakeRequest.status_code = 200
        fakeRequest.reason = 'OK'
        fakeRequest.json.return_value = self.valid_notification
        mock.return_value = fakeRequest
        tmp = client.push_msg()
        assert tmp[0] == 200
        assert tmp[1] == 'OK'
        assert tmp[2] == self.valid_notification

        self.payload['app_ids'] = ["1", "2"]

        mock.assert_called_with(client.api_url, 
                                headers=client.header,
                                json=self.payload)

    @patch('pbsonesignal.requests.post')
    def test_push_msg_app_id(self, mock):
        """Test push_msg with array app_id works."""
        client = PybossaOneSignal(app_id="1", api_key="key")
        fakeRequest = MagicMock()
        fakeRequest.status_code = 200
        fakeRequest.reason = 'OK'
        fakeRequest.json.return_value = self.valid_notification
        mock.return_value = fakeRequest
        tmp = client.push_msg()
        assert tmp[0] == 200
        assert tmp[1] == 'OK'
        assert tmp[2] == self.valid_notification

        self.payload['app_id'] = "1"

        mock.assert_called_with(client.api_url, 
                                headers=client.header,
                                json=self.payload)

    @patch('pbsonesignal.requests.post')
    def test_push_msg_include_player_ids(self, mock):
        """Test push_msg with array include_player_ids works."""
        client = PybossaOneSignal(app_id="1", api_key="key")
        fakeRequest = MagicMock()
        fakeRequest.status_code = 200
        fakeRequest.reason = 'OK'
        fakeRequest.json.return_value = self.valid_notification
        mock.return_value = fakeRequest
        tmp = client.push_msg(include_player_ids=["1"])
        assert tmp[0] == 200
        assert tmp[1] == 'OK'
        assert tmp[2] == self.valid_notification

        self.payload['app_id'] = "1"
        self.payload['include_player_ids'] = ["1"]

        mock.assert_called_with(client.api_url, 
                                headers=client.header,
                                json=self.payload)

    @patch('pbsonesignal.requests.post')
    def test_push_msg_include_send_after(self, mock):
        """Test push_msg with array send_after works."""
        client = PybossaOneSignal(app_id="1", api_key="key")
        fakeRequest = MagicMock()
        fakeRequest.status_code = 200
        fakeRequest.reason = 'OK'
        fakeRequest.json.return_value = self.valid_notification
        mock.return_value = fakeRequest
        tmp = client.push_msg(send_after="Thu Sep 24 2015 14:00:00 GMT-0700 (PDT)")
        assert tmp[0] == 200
        assert tmp[1] == 'OK'
        assert tmp[2] == self.valid_notification

        self.payload['app_id'] = "1"
        self.payload['send_after'] = "Thu Sep 24 2015 14:00:00 GMT-0700 (PDT)"

        mock.assert_called_with(client.api_url, 
                                headers=client.header,
                                json=self.payload)

    @patch('pbsonesignal.requests.post')
    def test_push_msg_include_delayed_option(self, mock):
        """Test push_msg with array delayed_option works."""
        client = PybossaOneSignal(app_id="1", api_key="key")
        fakeRequest = MagicMock()
        fakeRequest.status_code = 200
        fakeRequest.reason = 'OK'
        fakeRequest.json.return_value = self.valid_notification
        mock.return_value = fakeRequest
        tmp = client.push_msg(delayed_option="last-active")
        assert tmp[0] == 200
        assert tmp[1] == 'OK'
        assert tmp[2] == self.valid_notification

        self.payload['app_id'] = "1"
        self.payload['delayed_option'] = "last-active"

        mock.assert_called_with(client.api_url, 
                                headers=client.header,
                                json=self.payload)

    @patch('pbsonesignal.requests.post')
    @raises(CreateNotification)
    def test_push_msg_fail(self, mock):
        """Test push_msg works."""
        client = PybossaOneSignal(app_id="1", api_key="key")
        fakeRequest = MagicMock()
        fakeRequest.status_code = 400
        fakeRequest.reason = 'OK'
        fakeRequest.json.return_value = self.error_notification
        mock.return_value = fakeRequest
        tmp = client.push_msg()
        assert tmp[0] == 400
        assert tmp[1] == 'BadRequest'
        assert tmp[2] == self.error_notification
