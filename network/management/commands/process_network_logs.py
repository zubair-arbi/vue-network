# -*- coding: utf-8 -*-
"""
Parse network log files from the "network_data" directory and save the parsed data in the database.
"""

from __future__ import absolute_import, unicode_literals

import os

import pprint
from logging import getLogger

from django.core.management.base import BaseCommand
from django.conf import settings

from network.utils import NetworkLogFileParser


LOGGER = getLogger(__name__)
NETWORK_LOGS_DIR = os.path.join(settings.BASE_DIR, 'network_data')


class Command(BaseCommand):
    """
    Parse and save data from network log files in the "network_data" directory.
    """

    def handle(self, *args, **options):
        """
        Parse and save data from network log text files.
        """
        for log_file_name in os.listdir(NETWORK_LOGS_DIR):
            self.process_file(log_file_name)

    def process_file(self, log_file_name):
        """
        Parse network file.
        """
        if log_file_name.endswith('.txt'):
            log_file_parser = NetworkLogFileParser(NETWORK_LOGS_DIR, log_file_name)
            parsed_data = log_file_parser.extract_file_data()
            pprint.pprint(parsed_data)
