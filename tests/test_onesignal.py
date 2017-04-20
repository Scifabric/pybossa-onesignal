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

FakeRequest = namedtuple('FakeRequest', ['text', 'status_code', 'headers'])


class TestPybossaOnesignal(object):

    def create_fake_request(self, data, status=None, mimetype={'content-type': 'application/json'}):
        if status is None and data['status_code']:
            return FakeRequest(json.dumps(data), data['status_code'], mimetype)
        else:
            return FakeRequest(json.dumps(data), status, mimetype)

    def create_error_output(self, action, status_code, target,
                            exception_cls, exception_msg=None):
        error = dict(action=action,
                     status="failed",
                     status_code=status_code,
                     target=target,
                     exception_cls=exception_cls,
                     exception_msg=exception_msg)
        return error

    def check_error_output(self, res, err):
        for k in err.keys():
            assert err[k] == res[k], err

    @raises(AppIdMissing)
    def test_init_no_app_id(self):
        """Test init without app_id."""
        PybossaOneSignal(api_key="something")

    @raises(AppIdMissing)
    def test_init_no_app_ids(self):
        """Test init without app_ids."""
        PybossaOneSignal(api_key="something")

    @raises(AppIdDuplicate)
    def test_init_no_app_id_duplicates(self):
        """Test init using app_id and app_ids."""
        PybossaOneSignal(app_id="1", app_ids=["a"], api_key="something")

    @raises(TypeError)
    def test_init_no_api_key(self):
        """Test init without api_key."""
        PybossaOneSignal(app_id="1")

    def test_proper_init(self):
        """Test init adds header."""
        client = PybossaOneSignal(app_id="1", api_key="key")
        assert client.header['Content-Type'] == 'application/json; charset=utf-8'
        assert client.header['Authorization'] == 'Basic key'
