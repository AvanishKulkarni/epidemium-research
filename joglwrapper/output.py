from pathlib import Path
import csv
from joglwrapper import Project
from project import Member

'''Generates XLSX files from cached data'''
class Output:

    def __init__(self):
        pass

    '''Generates output CSV file with all information about a project'''
    def generate_project(self, index):
        pass
    
    '''Generates output CSV file with all information about a user'''
    def generate_user_activity(self, id, output_name):
        # Field Names
        csv_fields = ["type", "title", "summary"]

        

        for index in range(1, 7):
            with open(f'./joglwrapper/cache/{index}/users/') as f:
                cache_reader = Project(index)

                try:
                    member = Project.get_member(id)
                    needs_list = member.get_needs()
                    proposals_list = member.get_proposals()
                    
                except:
                    continue



        Path(f'./joglwrapper/output/{id}/').mkdir(parents=True, exist_ok=True)
        with open(f'./joglwrapper/output/user_{id}/{output_name}.csv', 'w', encoding='utf-8') as f:
            csvwriter = csv.writer(f)

            csvwriter.writerow(csv_fields)


