class FrozenClass(object):
    __is_frozen__ = False
    def __setattr__(self, key, value):
        if self.__is_frozen__ and not hasattr(self, key):
            raise TypeError( f"{type(self)} does not have attribute {key}, "
							 f"{type(self)} is a frozen class and cannot have attributes added after construction.\n"
							 "If you did not catch this error by accident, "
							 "you may disable this catch by setting __is_frozen__ to False" % self )
        object.__setattr__(self, key, value)