"""Find ports from input.

Read through logs and find and output port numbers that start with 'port' and are followed by a 1-5 digit number.

Usage:
  python FindPorts.py log1 log2 ...
  python FindPorts.py < log3

Discussion:
  From the samples provided, all port numbers are preceded by ‘port’ which makes it easier to find a port
  rather than any number from 1-65535 which may not be a port.  The characters between port and the number
  were ‘ ‘, ‘:’ and ‘”’.  We could have looked for exactly those and limited to 1-2 characters but allowing
  any characters between 0-3 seems like it will catch more port numbers as the variety of characters is
  potentially bigger than in the samples.  I've seen more accurate expressions that only capture 1-65535 but,
  if you find ‘port’ followed by a 1-5-digit number, then it might warrant inspection even if out of range.
"""

import re
import argparse
import sys


# find 'port' followed by a 0-3 characters and then a 1-5 digit number to catch more values of interest
find_ports = re.compile(r'port\D{0,3}(\d{1,5})', re.IGNORECASE)


def search_text(text):
    """Search text for ports and print port number

    Args:
        text: text to search for ports
    """
    ports = find_ports.findall(text)

    for port in ports:
        print(port)

def read_files(files):
    """Read each file's contents and search for ports

    Args:
        files: list of files

    Raises:
        Exception: An error occurred while opening, reading, or searching a file
    """

    for path in files:
        try:
            with open(path, 'r') as file:
                contents = file.read()
                search_text(contents)
        except FileNotFoundError:
            print(f"File not found: {path}")
        except Exception as e:
            print(f"An exception occurred processing {path}: {str(e)}")

def read_input():
    """Read redirected input from command line

    Raises:
        Exception: An error occurred while reading input from command line or searching a file
    """
    try:
        redirected_input = sys.stdin.read()
        search_text(redirected_input)
    except Exception as e:
        print(f"An exception occurred reading input: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get logs.")
    parser.add_argument("logs", nargs="*", help="List of logs to read.")

    args = parser.parse_args()
    file_list = args.logs

    if file_list:
        read_files(file_list)
    else:
        read_input()