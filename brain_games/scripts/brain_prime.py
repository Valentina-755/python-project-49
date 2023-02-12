#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), '../..'))
from brain_games import logic # NOQA
from brain_games.games import prime # NOQA


def main():
    name = logic.welcome()
    prime.condition()
    logic.round(prime.task(), name)


if __name__ == '__main__':
    main()
