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
Exceptions module for sending Web PUSH notifications.

This module exports:
    * AppIdMissing: OneSignal app_id string is missing.
    * AppIdsMissing: OneSignal app_ids array of strings is missing.
    * ApiKeyMissing: OneSignal api_key is missing.
"""

__all__ = ['AppIdsMissing', 'AppIdMissing', 'ApiKeyMissing', 'AppIdDuplicate',
           'CreateNotification', 'CreateApp', 'AuthKeyMissing',
           'ApiAuthKeysMissing']


class AppIdMissing(Exception):
    pass


class AppIdDuplicate(Exception):
    pass


class AppIdsMissing(Exception):
    pass


class ApiKeyMissing(Exception):
    pass


class AuthKeyMissing(Exception):
    pass


class ApiAuthKeysMissing(Exception):
    pass


class CreateNotification(Exception):
    pass


class CreateApp(Exception):
    pass
