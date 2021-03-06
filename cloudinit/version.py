# Copyright (C) 2012 Yahoo! Inc.
#
# Author: Joshua Harlow <harlowja@yahoo-inc.com>
#
# This file is part of cloud-init. See LICENSE file for license information.

__VERSION__ = "0.7.9"

FEATURES = [
    # supports network config version 1
    'NETWORK_CONFIG_V1',
]


def version_string():
    return __VERSION__

# vi: ts=4 expandtab
