# task for you!!!
class Calculator:
    brand = 'Casio MS990'
    def add(self, num1, num2):
        sum = num1 + num2
        text = f'Total sum is: {sum}'
        print(text)
    def deduct(self, num1, num2):
        deduct = num1 - num2
        text = f'Total deduct is: {deduct}'
        print(text)
    def multify(self, num1, num2):
        multi = num1 * num2
        text = f'Total multi is: {multi}'
        print(text)

calculator = Calculator()
calculator.add(20, 30)
calculator.deduct(30, 10)
calculator.multify(20, 30)

    # deduct method

    # multiply method

    # divide method