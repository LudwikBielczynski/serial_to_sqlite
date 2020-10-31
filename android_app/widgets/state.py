from copy import deepcopy
from typing import Any, Dict, List

DEBUG = False

relays = [] # type: List[Dict[str, Any]]

host = 'dzialka-kaluszyn.ddns.net'
username = ''
password = ''

relay = {'channel': '',
         'section_name': '',
         'start': '',
         'end': '',
         'weekday': [],
        } # type: Dict[str, Any]

relays_cache = deepcopy(relays)
relay_cache = deepcopy(relay)

communicator = 'free'
login_transition = False
