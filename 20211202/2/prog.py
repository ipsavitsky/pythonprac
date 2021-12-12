from __future__ import annotations
from typing import get_type_hints

class check(type):
    def __init__(self, *args, **kwargs):
        def checker(self):
            al = get_type_hints(self)
            for elem in al.items():
                if not isinstance(getattr(self, elem[0], None), elem[1]):
                    return False
            return True
        self.check_annotations = checker
        return super().__init__(*args, **kwargs)


import sys
exec(sys.stdin.read())