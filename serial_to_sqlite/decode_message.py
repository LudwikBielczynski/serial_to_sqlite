from typing import Tuple

def decode_message(message: str) -> Tuple[str, int, float]:
    '''Function used to decode the message'''
    try:
        tx_message = message.split('=')[1]
        transmitter_name = tx_message.split(';')[0]
        soil_humidity_value = int(tx_message.split(';')[1])
        battery_state = 1.

    except IndexError:
        print(f'Wrong message format: {message}')

    return (transmitter_name, soil_humidity_value, battery_state)
