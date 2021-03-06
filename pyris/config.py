# coding: utf-8

"""Pyris configuration

Retrieve user and password from the YAML configuration file for the database
access
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import os
import io

from yaml import load as yload


_cfgfile = os.environ.get('PYRIS_APP_SETTINGS')

if _cfgfile is not None:
    with io.open(_cfgfile, 'r') as fobj:
        DATABASE = yload(fobj.read()).get('database', {})
else:
    DATABASE = {"USER": os.environ["USER"], "DBNAME": os.environ["USER"]}
