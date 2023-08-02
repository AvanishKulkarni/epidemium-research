from pathlib import Path
import csv
from joglwrapper.project import Project
from joglwrapper.member import Member

'''Generates XLSX files from cached data'''
class Output:

    def __init__(self):
        pass

    '''Generates output CSV file with all information about a project'''
    def generate_project(self, index):
        pass
    
    '''Generates output CSV file with all information about a user'''
    def generate_user_activity(self, user_id, output_name):
        Path(f'./joglwrapper/output/user_{user_id}/').mkdir(parents=True, exist_ok=True)

        activities = []

        for index in range(1, 7):
            cache_reader = Project(index)

            member = cache_reader.get_member(user_id)

            try: 
                activities += member.get_proposals() 
                activities += member.get_needs() 
                activities += member.get_spaces()
                activities += member.get_programs()
                activities += member.get_peer_reviews()
                activities += member.get_projects()
                activities += member.get_challenges()
            except:
                break

        

            

        with open(f'./joglwrapper/output/user_{user_id}/{output_name}.csv', 'w', encoding='utf-8', newline='') as f:
            csvwriter = csv.writer(f)

            csv_fields = ["type", "title", "summary"]        
            csvwriter.writerow(csv_fields)

            write_list = []

            for activity in activities:
                # TODO Clean random code from summaries
                write_list.append([f"{activity.type}", f"{activity.title}", f"{activity.summary}"])

            csvwriter.writerows(write_list)



