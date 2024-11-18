class PhoneNumber:
    def __init__(self, number):
        self.number = (number.
                       replace("(", "").
                       replace(")", "").
                       replace(".", "").
                       replace("-", "").
                       replace("+", "").
                       replace(" ", "")
                       )
        self.digitCheck()
        self.area_code = self.area_code()

    def digitCheck(self):
        if len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(self.number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if any(char == '@' or char == '!' or char == ':' for char in self.number):
            raise ValueError("punctuations not permitted")
        if any(char.isalpha() for char in self.number):
            raise ValueError("letters not permitted")
        if len(self.number) == 10:
            if self.number[0] == '1':
                raise ValueError("area code cannot start with one")
            if self.number[0] == '0':
                raise ValueError("area code cannot start with zero")
            if self.number[3] == '1':
                raise ValueError("exchange code cannot start with one")
            if self.number[3] == '0':
                raise ValueError("exchange code cannot start with zero")
        if len(self.number) == 11:
            if self.number[0] != '1':
                raise ValueError("11 digits must start with 1")
            if self.number[1] == '1':
                raise ValueError("area code cannot start with one")
            if self.number[1] == '0':
                raise ValueError("area code cannot start with zero")
            if self.number[4] == '1':
                raise ValueError("exchange code cannot start with one")
            if self.number[4] == '0':
                raise ValueError("exchange code cannot start with zero")
            self.number = self.number[1:]

    def area_code(self):
        if len(self.number) == 10:
            res = self.number[0:3]
            return res
        if len(self.number) == 11:
            res = self.number[1:4]
            return res

    def pretty(self):
        return "(" + self.number[0:3] + ")-" + self.number[3:6] + "-" + self.number[6:]
