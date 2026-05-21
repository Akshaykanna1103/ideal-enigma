"""A module for print out """

def double_it(x: int | float | str |list[int | float | str]) -> None:
    """this a Docstring"""

    return x + x

if __name__ == "__main__":
    double_it(2)
    print("Final line in this module - The end")
    