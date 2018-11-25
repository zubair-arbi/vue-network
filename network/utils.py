"""
Helper methods for reading network logs and extraction of required data from them.
"""

from logging import getLogger


LOGGER = getLogger(__name__)


class NetworkLogFileParser(object):
    """
    Class to extract information from the provided network log file.
    """
    def __init__(self, base_dir, file_name):
        """
        Setup file parsing.

        Arguments:
            base_dir (str): Network logs files directory.
            file_name (str): Network log file name to extract information.

        """
        self.base_dir = base_dir
        self.file_name = file_name

    def extract_file_data(self):
        """
        Iterate over each line and extract Areas and Systems connected to current system.

        Example extracted data: {
            'PE-L3Agg-Unay-602-2': {
                'areas': [
                    '8005',
                    '4400',
                    '4444'
                ],
                'connected_systems': [
                    'MetroCore-PTX5K-Bur-601-1-re0',
                    'MetroCore-PTX5K-Bur-601-1-re0',
                    'MetroCore-PTX5K-Abar-422-1-re0',
                    'MetroCore-PTX5K-Abar-422-1-re0',
                    'PRE-AGG9K-603-00-000-1.stc.com.sa'
                ]
            }
        }
        """
        current_system = self.file_name.rstrip('.txt')
        current_system_areas = []
        connected_systems = []
        log_file = '{base_dir}/{file_name}'.format(
            base_dir=self.base_dir, file_name=self.file_name
        )
        with open (log_file, 'rt') as reader:
            for line in reader:
                line_text = line.strip()
                if 'net ' in line_text:
                    # Find network mask with format "49.4401.1921.6811.5185.00"
                    network_mask = line_text.split('net ')[-1]
                    # Extract area "4401" from the network mask 49.4401.1921.6811.5185.00
                    try:
                        area = network_mask.split('.')[1]
                        current_system_areas.append(area)
                    except IndexError:
                        # Ignore this error since this line didn't have a valid network mask
                        pass
                    continue

                if 'System Name: ' in line_text:
                    system_name = line_text.split('System Name: ')[-1]
                    connected_systems.append(system_name)

        return {
            current_system: {
                'areas': current_system_areas,
                'connected_systems': connected_systems,
            }
        }


