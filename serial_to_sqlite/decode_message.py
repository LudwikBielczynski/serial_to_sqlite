from typing import Tuple, Optional

def decode_message(message: str) -> Tuple[str, Optional[int], Optional[float]]:
    '''Function used to decode the message'''
    transmitter_name = 'Tx?'
    soil_humidity_value = None
    battery_state = None

    try:
        tx_message = message.split('=')[1]

        transmitter_name = tx_message.split(';')[0]
        soil_humidity_value = int(tx_message.split(';')[1])
        battery_state = float(tx_message.split(';')[2])

    except IndexError:
        print(f'Wrong message format: {message}')

    return (transmitter_name, soil_humidity_value, battery_state)
