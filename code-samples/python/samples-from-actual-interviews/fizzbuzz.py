"""

write a program prints all numbers that are multiples of 2 with the word fizz
and all numbers that are multiples of 5 with the word buzz if the number is both
is prints fizzbuzz


"""

def main():
    for number in range(1,101):
        return_value = ""

        if number % 2 == 0:
            return_value = return_value + "fizz"

        if number % 5 == 0:
            return_value = return_value + "buzz"

        if return_value != "":
            print("{} {}".format(number, return_value))


if __name__ == "__main__":
    main()
