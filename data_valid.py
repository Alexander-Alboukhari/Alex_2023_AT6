
class Data_Valid:
    def validate(self, list):
        valid_int = []
        for item in list:
            if item.isdigit() and int(item) > 0:
                valid_int.append(int(item))
        return valid_int
validator = Data_Valid()

list = ["10", "-5", "3.14", "hello", "42", "0", "100"]

valid_numbers = validator.validate(list)

print("Valid positive integers:", valid_numbers)