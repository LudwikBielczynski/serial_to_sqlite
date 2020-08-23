import json

from common.shares import RELAYS_CONFIG_PATH

def load_channel_section_name_map():
    ''''Channel-section name mapping is stored locally in a config'''
    with open(RELAYS_CONFIG_PATH, 'r') as json_data:
        relays_config_json = json.load(json_data)

    channel_section_name_map = {
        channel_info['channel_nr']: channel_info['section_name']
        for channel_info in relays_config_json
        }
    return channel_section_name_map