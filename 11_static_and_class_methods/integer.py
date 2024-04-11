class Integer:

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"

        return cls(int(value))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"

        return cls(int(value))


