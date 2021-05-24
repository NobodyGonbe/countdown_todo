# -*- coding: utf-8 -*-

import argparse
from typing_extensions import ParamSpecArgs







if __name__ == '__main__':
    # use cmd setting
    parser = argparse.ArgumentParser(description = 'task to change date order ToDo ')
    parser.add_argument('--todo', required = True, help = 'yyyymmddhhmmToDo')
    parser.add_argument('--deltodo', help = 'delete column no')
    parser.add_argument('--regtodo', help = 'regular schedule')
    parser.add_argument('--reglist', help = 'regular schedule list')
    parser.add_argument('--delreg', help = 'regular scheduke list column no')
    args = parser.parse_args()

    todo_list = []
    regular_list = []

    