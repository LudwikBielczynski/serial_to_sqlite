import widgets.state
from widgets.info_bubble import print_on_info_bubble

def validate_time_input(time_str):
    '''Checks if the string representing time is well formed'''
    is_valid = True

    if (set(time_str) - set('1234567890:')) == set():
        if ':' in time_str:
            hours_str = time_str.split(':')[0]
            if len(hours_str) > 2:
                is_valid = False

            hours = int(hours_str)
            if (hours >= 24) | (hours < 0):
                is_valid = False

            minutes_str = time_str.split(':')[1]
            if len(minutes_str) != 2:
                is_valid = False

            minutes = int(minutes_str)
            if (minutes >= 60) | (minutes < 0):
                is_valid = False
        else:
            is_valid = False
    else:
        is_valid = False
    return is_valid

def time_validation(instance):
    is_valid = validate_time_input(instance.text)
    for relay_nr, relay in enumerate(widgets.state.relays):
        if relay['channel'] == widgets.state.relay['channel']:
            if is_valid:
                widgets.state.relays[relay_nr]['start'] = instance.text
            else:
                print_on_info_bubble('The input was not valid')
                instance.text = widgets.state.relays[relay_nr]['start']
