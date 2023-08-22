from joglwrapper import Reader
from joglwrapper import Project
from joglwrapper import Output
from pathlib import Path

import csv

with open("output.csv", 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    for index in range(1, 7):
        project = Project(index)

        writer.writerow(
            [
                f'{project.title} ({project.id})',
                f'{project.short_description}'
            ]
        )

        for member in project.get_members():
            writer.writerow(
                [
                    '',
                    f'{str(member)}',
                ]
            )


            for activity in member.get_activities():
                writer.writerow(
                    [
                        '','',
                        f'{activity.type}',
                        f'{activity.title} ({activity.id})',
                        f'{activity.summary}'
                    ]
                )
            


