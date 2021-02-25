from .base import *

# settings for local
try:
    from .local import *
except:
    pass


# settings for production
try:
    from .production import *
except:
    pass
