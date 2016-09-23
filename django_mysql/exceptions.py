# -*- coding:utf-8 -*-
from __future__ import absolute_import, division


class TimeoutError(Exception):
    """
    Indicates a database operation timed out in some way.
    """
    pass
