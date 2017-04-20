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
