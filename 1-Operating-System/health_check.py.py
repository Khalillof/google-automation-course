#!/usr/bin/env python3
import shutil
import psutil
import socket
import os
import sys

def check_reboot():
    """ Return True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_root_disk_full():
    """ Return True if the root partation is full."""

    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_disk_full(disk, min_gb, min_percent):
    """Return True if there isn't enough disk space , false otherwise """

    du = shutil.disk_usage(disk)
    percent_free = du.free / du.total * 100
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    return psutil.cpu_percent(1) > 75

def check_momory():
    # 500MB = 52428800.0   
   return psutil.virtual_memory().available <= 52428800.0
       
def check_localhost():
    """ will return true if localhost not equal '127.0.0.1'  """
    localhost = socket.gethostbyname('localhost')
    if localhost == '127.0.0.1':
       return False
    else:
       return True

def check_no_network():
    """ will Return True if it fail to resolve google's URL, False otherwise """
    try:
       socket.gethostbyname('google.com')
       return False
    except:
        return True

def main():
    checks=[
        (check_reboot,"server is Pending Reboot"),
        (check_root_disk_full,"Error - Available disk space is less than 20%"),
        (check_no_network,"no working network"),
        (check_momory, "Error - Available memory is less than 500MB")
        (check_cpu_usage,"Error - CPU usage is over 80%"),
        (check_localhost,"Error - localhost cannot be resolved to 127.0.0.1"),
        ]
    everything_ok=True

    for check, msg in checks:
        if check():
            print(msg)
            everything_ok=False

    if not everything_ok:
       sys.exit(1)
    else:
       print("every thing is OK")
       sys.exit(0)

if __name__ == "__main__":
    main()
