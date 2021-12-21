def objcount(cl):
    class counted_class(cl):
        counter = 0
        def __init__(self, *args, **kwargs):
            self.__class__.counter += 1
            super().__init__(*args, *kwargs)

        def __del__(self):
            self.__class__.counter -= 1
            if hasattr(super(), '__del__'):
                super().__del__()
    # print(cl.__class__.__name__)
    counted_class.__name__ = cl.__name__
    return counted_class

import sys
exec(sys.stdin.read())