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
from pbsonesignal import PybossaOneSignal
from pbsonesignal.exceptions import *
from nose.tools import raises
from mock import patch, MagicMock


class TestPybossaOnesignal(object):

    error_app = {'errors': ['error']}

    valid_app = {u'safari_icon_16_16': u'16x16.png', 
                 u'chrome_web_gcm_sender_id': u'', 
                 u'site_name': None, 
                 u'safari_site_origin': None, 
                 u'safari_icon_32_32': u'16x16@2x.png', 
                 u'safari_apns_certificate': None, 
                 u'updated_at': u'2017-04-20T14:03:05.985Z', 
                 u'basic_auth_key': u'key', 
                 u'messageable_players': 0, 
                 u'id': u'id', 
                 u'safari_icon_256_256': u'128x128@2x.png', 
                 u'chrome_web_origin': u'https://scifabric.com', 
                 u'safari_push_id': None, 
                 u'safari_icon_64_64': u'32x32@2x.png', 
                 u'apns_certificates': None, 
                 u'chrome_web_default_notification_icon': u'https://scifabric.com/img', 
                 u'name': u'name', u'gcm_key': None, 
                 u'created_at': u'2017-04-20T14:03:05.883Z', 
                 u'chrome_web_sub_domain': u'', 
                 u'players': 0, u'apns_env': None, 
                 u'chrome_key': None, 
                 u'chrome_web_key': u'(OneSignal Shared Google Server API Key)', 
                 u'safari_icon_128_128': u'128x128.png'}

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
    def test_create_app(self, mock):
        """Test create_app works."""
        client = PybossaOneSignal(app_id="1", api_key="algo", auth_key="key")
        fakeRequest = MagicMock()
        fakeRequest.status_code = 200
        fakeRequest.reason = 'OK'
        fakeRequest.json.return_value = self.valid_app
        mock.return_value = fakeRequest
        tmp = client.create_app('name', 'https://scifabric.com', 'https://scifabric.com/img')
        assert tmp[0] == 200
        assert tmp[1] == 'OK'
        assert tmp[2] == self.valid_app

    @raises(CreateApp)
    @patch('pbsonesignal.requests.post')
    def test_create_app_errors(self, mock):
        """Test create_app errors works."""
        client = PybossaOneSignal(app_id="1", api_key="algo", auth_key="key")
        fakeRequest = MagicMock()
        fakeRequest.status_code = 400
        fakeRequest.reason = 'Bad Status'
        fakeRequest.json.return_value = self.error_app
        mock.return_value = fakeRequest
        tmp = client.create_app('name', 'https://scifabric.com', 'https://scifabric.com/img')
        assert tmp[0] == 400
        assert tmp[1] == 'Bad Status'
        assert tmp[2] == self.error_app
