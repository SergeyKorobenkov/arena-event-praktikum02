class NameValid:
    def __get__(self, instance, class_):
        return self.val

    def __set__(self, instance, value):
        if isinstance(value, str):
            self.val = value
        else:
            raise TypeError(f"{value} is not a string")


class ProtectValid:
    def __get__(self, instance, class_):
        return self.val

    def __set__(self, instance, value):
        if isinstance(value, float):
            self.val = value
        else:
            raise TypeError(f"{value} is not a float")


class ProtectThingValid(ProtectValid):
    def __set__(self, instance, value):
        if isinstance(value, float) and 0 <= value <= 0.1:
            self.val = value
        elif not isinstance(value, float):
            raise TypeError(f"{value} is not a float")
        else:
            raise ValueError(f"Attribute should be between 0 and 0.1")


class DamageValid:
    def __get__(self, instance, class_):
        return self.val

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.val = value
        else:
            raise TypeError(f"{value} is not a int")


class HpValid:
    def __get__(self, instance, class_):
        return self.val

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.val = value
        else:
            raise TypeError(f"{value} is not a int")
