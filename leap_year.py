#!/usr/bin/env python3
# Created by: Kent Gatera
# Created on: Oct 19
# This program checks if a year is a leap year.


def main():
    year_input = input("What year do you think is a leap year?: ")

    try:

        int_year_input = int(year_input)
        # Year must be greater than 1582 - the first year of the Gregorian calendar.
        if int_year_input < 1582:
            print(
                "{} must be part of the Gregorian calendar (1582-Today)".format(
                    int_year_input
                )
            )
            # this line checks if the year has leap year potential.
        if int_year_input % 4 == 0:
            if (int_year_input % 100 == 0) and (int_year_input % 400 == 0):
                print("{} is a leap year.".format(int_year_input))
            # Years divisible by 100 are not leap years unless hey are also divisible by 400.
            elif int_year_input % 100 == 0:
                print("{} is NOT a leap year.".format(int_year_input))
        else:
            print("{} is NOT a leap year.".format(int_year_input))
    except:
        print(year_input + " is not a valid answer, enter a number.")


# Running the program.
if __name__ == "__main__":
    main()
