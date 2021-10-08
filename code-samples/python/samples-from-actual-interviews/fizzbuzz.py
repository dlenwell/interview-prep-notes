"""

write a program prints all numbers that are multiples of 3 with the word fizz
and all numbers that are multiples of 5 with the word buzz if the number is both
is prints fizzbuzz


"""

def main():
    for number in range(1,101):
        line_output = ""

        if number % 3 == 0:
            line_output = "fizz"

        if number % 5 == 0:
            line_output = line_output + "buzz"

        if return_value != "":
            print("{}:  {}".format(number, line_output))


if __name__ == "__main__":
    main()
