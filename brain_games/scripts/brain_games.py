#!/usr/bin/env python3
import sys
import os
import cli
sys.path.insert(0, os.path.join(os.getcwd(), '..'))


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    cli.welcome_user()


if __name__ == '__main__':
    main()
