
class IOCContainer:
    def __init__(self):
        self._instances = {}

    def get_instance(self, cls):
        instance = self._instances.get(cls)
        if not instance:
            instance = cls()
            self._instances[cls] = instance
        return instance
