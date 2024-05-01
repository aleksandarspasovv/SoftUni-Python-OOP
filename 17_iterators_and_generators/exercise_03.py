class vowels:

    def __init__(self, string):
        self.string = string
        self.vowels_list = ['a', 'e', 'o', 'u', 'y', 'i']
        self.vowels_values = [x for x in self.string if x.lower() in self.vowels_list]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_values):
            return self.vowels_values[self.index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
