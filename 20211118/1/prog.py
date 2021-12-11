def objcount(cl):
    class counted_class(cl):
        counter = 0
        def __init__(self, *args, **kwargs):
            super().__init__()
            self.__class__.counter += 1

        def __del__(self):
            if hasattr(super(), '__del__'):
                super().__del__()
            self.__class__.counter -= 1

    return counted_class

import sys
exec(sys.stdin.read())