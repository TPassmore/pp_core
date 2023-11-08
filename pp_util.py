from datetime import datetime

import os, sys
import signal



def log(msg):     return "[TrailerFarm] %s [Log    ]: %s" % (datetime.now().strftime("[%d/%m/%Y] [%H:%M:%S]"), msg)
def error(msg):   return "[TrailerFarm] %s [Error  ]: %s" % (datetime.now().strftime("[%d/%m/%Y] [%H:%M:%S]"), msg)
def warning(msg): return "[TrailerFarm] %s [Warning]: %s" % (datetime.now().strftime("[%d/%m/%Y] [%H:%M:%S]"), msg)
def debug(msg):   return "[TrailerFarm] %s [Debug  ]: %s" % (datetime.now().strftime("[%d/%m/%Y] [%H:%M:%S]"), msg)
def fatal(msg):   return "[TrailerFarm] %s [Fatal  ]: %s" % (datetime.now().strftime("[%d/%m/%Y] [%H:%M:%S]"), msg)

def print_log(msg): print(log(msg))
def print_error(msg): print(error(msg))
def print_warning(msg): print(warning(msg))
def print_debug(msg): print(debug(msg))
def print_fatal(msg): print(fatal(msg))


def to_underscores(string:str):
    return string.replace(' ', '_')

def to_spaces(string:str):
    return string.replace('_', ' ')

def kill_pid(pid):
    try:
        os.kill(pid, signal.SIGTERM)
    except Exception as e:
        print(e)

# def get_system_os():
#     return sys.platform()