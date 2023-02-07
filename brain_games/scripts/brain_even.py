#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(),'..'))
import logic 
from games import even



def main():
    name = logic.welcome()
    even.condition()
    logic.round(even.task(), name)



if __name__ == '__main__':
    main()
