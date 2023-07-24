from datetime import datetime
from calendar import day_name

def get_birthdays_per_week(users: list[dict]) -> None:
    '''
    Bringing this week's birthdays to the console
    '''

    birthdays = {}
    for day in day_name:
        birthdays[day] = ''

    time = datetime.now()
    week = [day for day in range(time.day - time.weekday(),\
                                 time.day - time.weekday() + 7)]
    for user in users:
        if user['birthday'].month == time.month and \
           user['birthday'].day in week:

            weekday = day_name[user['birthday'].weekday()]
            if birthdays[weekday]:
                birthdays[weekday] += ', ' + user['name']
            else:
                birthdays[weekday] += user['name']
    for key, value in birthdays.items():
        if value:
            print(f'{key}: ', value)
    

if __name__ == '__main__':
    users = [
        {
            'name': 'Bill',
            'birthday': datetime(year=1996, month=7, day=25)
        },
        {
            'name': 'Ann',
            'birthday': datetime(year=1996, month=7, day=27)
        },
        {
            'name': 'Rich',
            'birthday': datetime(year=2005, month=7, day=25)
        },
    ]

    get_birthdays_per_week(users)