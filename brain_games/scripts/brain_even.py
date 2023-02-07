#!/usr/bin/env python3
import sys
import os
import logic
from games import even
sys.path.insert(0, os.path.join(os.getcwd(), '..'))


def main():
    name = logic.welcome()
    even.condition()
    logic.round(even.task(), name)


if __name__ == '__main__':
    main()
