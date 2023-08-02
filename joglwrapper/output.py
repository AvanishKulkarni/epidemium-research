import os
from pathlib import Path
import json
import csv

'''Generates XLSX files from cached data'''
class Output:

    def __init__(self):
        pass

    '''Generates output CSV file with all information about a project'''
    def generate_project(self, index):
        pass
    
    '''Generates output CSV file with all information about a user'''
    def generate_user(self, id, output_name):
        # Field Names
        fields = ["type", "title", "summary"]

        Path(f'./joglwrapper/output/{id}/').mkdir(parents=True, exist_ok=True)
        with open(f'./joglwrapper/output/{id}/{output_name}.csv', 'w', encoding='utf-8') as f:
            csvwriter = csv.writer(f)

            csvwriter.writerow(fields)


