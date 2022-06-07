def transaction(n):
    num = n
    while True:
        num += 1
        yield num

class Account:
    transaction_counter = transaction(0)

    def __init__(self, account_number, first_name, last_name):
        self._account_number = account_number
        self._first_name = first_name
        self._last_name = last_name
    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = self.validate_name(first_name, "First Name")

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = self.validate_name(last_name, "Last Name")
    
    def validate_name(value, field_tittle):
        if len(str(value)).strp() == 0:
            raise ValueError(f"{field_tittle} cannot be empty")
        return value
    