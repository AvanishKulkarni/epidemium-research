import os
from pathlib import Path
import json
import csv

'''Generates XLSX files from cached data'''
class Output:

    def __init__(self):
        Path(f'./joglwrapper/output/').mkdir(parents=True, exist_ok=True)

    '''Generates output CSV file with all information about a project'''
    def generate_project(self, index):
        pass
    
    '''Generates output CSV file with all information about a user'''
    def generate_user(self, id):
        pass

