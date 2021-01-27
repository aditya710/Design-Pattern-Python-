class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
    """The Borg design pattern"""
    

class Singleton(Borg):

    """The singleton class"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


x = Singleton(HTTP = "HyperText Transfer Protocol")
print(x)

y = Singleton(FTP = "File Transfer Protocol")
print(y)

