#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), '../..'))
from brain_games import logic
from brain_games.games import calc


def main():
    name = logic.welcome()
    calc.condition()
    logic.round(calc.task(), name)


if __name__ == '__main__':
    main()
