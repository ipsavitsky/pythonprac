def objcount(cl):
    class counted_class(cl):
        cl.counter = 0
        def __init__(self, *args, **kwargs):
            cl.counter += 1
            try:
                super().__init__(*args, *kwargs)
            except:
                super().__init__()

        def __del__(self):
            cl.counter -= 1
            if hasattr(super(), '__del__'):
                super().__del__()
    counted_class.__name__ = cl.__name__
    return counted_class

import sys
exec(sys.stdin.read())