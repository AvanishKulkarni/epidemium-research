from pathlib import Path
import csv
import re
from joglwrapper.project import Project
from joglwrapper.member import Member

'''Generates XLSX files from cached data'''
class Output:

    def __init__(self):
        self.cleaner = re.compile('<.*?>')

    '''Generates output CSV file with all information about a project'''
    def generate_project(self, index, output_name):
        Path(f'./joglwrapper/output/project_{index}/').mkdir(parents=True, exist_ok=True)

        with open(f'./joglwrapper/output/project_{index}/{output_name}.csv', 'w', encoding='utf-8', newline='') as f:
            csvwriter = csv.writer(f)
            project = Project(index)

            header = ['title', 'summary']

            csvwriter.writerow(header)
            csvwriter.writerow([f'{project.title}', f'{project.short_description}'])
            csvwriter.writerow(['members:'])
            csvwriter.writerow(['id', 'name', 'bio', 'affiliation'])
            
            for member in project.get_members():
                csvwriter.writerow([member.id, f'{member.first_name} {member.last_name}', member.short_bio, member.affiliation])
    
    '''Generates output CSV file with all information about a user'''
    def generate_user(self, user_id, output_name):
        Path(f'./joglwrapper/output/user_{user_id}/').mkdir(parents=True, exist_ok=True)

        activities = []

        for index in range(1, 7):
            cache_reader = Project(index)

            member = cache_reader.get_member(user_id)

            try:
                activities += member.get_proposals() 
            except:
                pass

            try:
                activities += member.get_needs() 
            except:
                pass

            try:
                activities += member.get_spaces()
            except:
                pass

            try:
                activities += member.get_programs()
            except:
                pass

            try:
                activities += member.get_peer_reviews()
            except:
                pass

            try:
                activities += member.get_projects()
            except:
                pass

            try:
                activities += member.get_challenges()
            except:
                pass

            if len(activities) > 0:
                break
               
        with open(f'./joglwrapper/output/user_{user_id}/{output_name}.csv', 'w', encoding='utf-8', newline='') as f:
            csvwriter = csv.writer(f)

            csv_fields = ["type", "title", "summary"]        
            csvwriter.writerow(csv_fields)

            write_list = []

            for activity in activities:

                unclean_text = activity.summary

                clean_text = re.sub(self.cleaner, '', unclean_text)

                write_list.append([f"{activity.type}", f"{activity.title}", f"{clean_text}"])

            csvwriter.writerows(write_list)

    '''Generates output CSV files for all users in a project'''
    def generate_all_users(self, index):
        for user in (project := Project(index)).get_members():
            self.generate_user(user.id, f'project_{project.id}_user_{user.id}')

    def generate_meta(self):
        Path(f'./joglwrapper/output/').mkdir(parents=True, exist_ok=True)

        with open(f'./joglwrapper/output/meta.csv', 'w', encoding='utf-8', newline='') as f:
            csvwriter = csv.writer(f)

            for index in range(1, 7):
                project = Project(index)

                csvwriter.writerow([f'project id: {project.id}'])

                row_2 = [
                    'member_id',
                    'proposal',
                    'need',
                    'space',
                    'program',
                    'peer_review',
                    'project',
                    'challenge',
                ]

                csvwriter.writerow(row_2)

                for member in project.get_members():
                    csv_row = [
                        member.id,
                        len(member.get_proposals()),
                        len(member.get_needs()),
                        len(member.get_spaces()),
                        len(member.get_programs()),
                        len(member.get_peer_reviews()),
                        len(member.get_projects()),
                        len(member.get_challenges()),
                    ]

                    csvwriter.writerow(csv_row)

                csvwriter.writerow([])
                    
