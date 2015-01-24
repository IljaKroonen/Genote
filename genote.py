from time import sleep
from re import sub
from sys import argv, exit

from autopy.mouse import click, move, toggle
from autopy.key import tap, MOD_SHIFT, MOD_CONTROL, K_DELETE

BEGIN_X = 900
BEGIN_Y = 500
END_X = 1000
END_Y = 500
def select_sequence_portion():
    move(BEGIN_X, BEGIN_Y)
    toggle(True)
    move(END_X, END_Y)
    toggle(False)
    sleep(0.1)

BUTTON_X = 1100
BUTTON_Y = 85
def click_annotate_button():
    move(BUTTON_X, BUTTON_Y)
    click()
    sleep(0.1)

def type_string(s):
    i = 0
    while i < len(s):
        if s[i].isdigit() or s[i] == "/":
            tap(s[i], MOD_SHIFT)
        else:
            tap(s[i])
        i = i + 1
    sleep(0.1)

INTERVAL_X = 1100
INTERVAL_Y = 450
def double_click_interval():
    move(INTERVAL_X, INTERVAL_Y)
    click()
    move(INTERVAL_X, INTERVAL_Y)
    click()
    sleep(0.1)

def ok():
    tap('\n')
    sleep(0.1)
    tap('\n')
    sleep(0.1)

def tab():
    tap('\t')
    sleep(0.1)

def clear_field():
    tap('a', MOD_CONTROL)
    tap(K_DELETE)
    sleep(0.1)

def process(begin, end, name, family):
    select_sequence_portion()
    click_annotate_button()
    type_string(name)
    tab()
    clear_field()
    type_string(family)
    double_click_interval()
    type_string(str(begin))
    tab()
    tab()
    clear_field()
    type_string(str(end))
    ok()

if len(argv) != 2:
    print 'Usage: ./launch target_file'
    exit(1)
    
with open(argv[1], 'r') as f:
    f.readline()
    f.readline()
    f.readline()
    
    for line in f:
        spl = sub(' +', ' ', line).strip().split(' ')
        print
        process(int(spl[5]), int(spl[6]), spl[9], spl[10])