import pprint
import sys
import os
import json
import time
from pprint import pprint
import requests
import datetime
import numpy as np
import re
import glob


regexRule = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

def write_file(file, data):
    with open(file, 'w') as outfile:
        outfile.write(data)

def read_file(file):
    with open(file, 'r') as outfile:
        return outfile.read()
        
