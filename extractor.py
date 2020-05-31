"""
Author: DracoY

Extracts emails from a string using regex.
"""
import re

def extract_email(string: str):
    """ Extracts email from a string. """
    pattern = r"([\w\d\.-]+)@([\w]+)\.\w+"

    if match:= re.search(pattern, string):
        return match.group()


def extract_date(string: str):
    """ Extracts date from string. """
    pattern = r"(([\d]?)([\d])([/-])){1,2}([\d]{2,4})"

    if match:= re.search(pattern, string):
        return match.group()


def main():
    email = "My email is example@gmail.com."
    print(extract_email(email))

    date = "Today's date is 31-05-2020"
    print(extract_date(date))


if __name__ == "__main__":
    main()
