from typing import Dict

class HttpRequest:
    def __init__(self, body: Dict = None, parm: Dict = None) -> None:
        self.body = body
        self.parm = parm

    

