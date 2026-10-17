class Entity_adapter[R]:
    """
    R - means record type
    Adapter class for converting to database entities or vice versa.
    """

    def __init__(self, source_entity, new_type, **adapted_methods):
        self.source = source_entity
        self.new_type = new_type
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__

    def __check_for_type(self):
        """
        Private function for checking type of source object.
        Return true if kindle history entity or false otherwise
        :return: boolean
        """
        if isinstance(self.source, self.new_type):
            return True
        return False

    def convert_to_database_entity(self):
        if not self.__check_for_type():
            return self.source
        else:
            return R()
