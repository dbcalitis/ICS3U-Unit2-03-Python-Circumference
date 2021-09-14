#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sep 2021
# This program calculates the circumference
#    with the radius given by the user

import constants


def main():
    # this function calculates the circuference

    # input
    radius = int(input("Enter the radius of the circle (cm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print(
        "The circumference of a circle with {0} cm radius is {1} cm".format(
            radius, circumference
        )
    )

    print("\nDone.")


if __name__ == "__main__":
    main()
