#! /usr/bin/env python3
# Author: PDalal
# Version: 1.0
# Description: This script will demo HowTo use system exit
"""
    DocString
"""

import sys
#sys.exit(0) # success
#sys.exit(1) # failure 1 - 255
try:
    sys.exit(1)
except SystemExit:
    print("exited")

