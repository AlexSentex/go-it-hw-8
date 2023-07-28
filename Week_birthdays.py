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
    ord_sat = time.toordinal() - time.weekday() + 5
    week = [day for day in range(ord_sat, ord_sat + 7)]
    
    for user in users:
        birthday = datetime(time.year, user['birthday'].month, user['birthday'].day)
        if birthday.toordinal() in week:
            
            day_num = birthday.weekday()
            if day_num > 4:
                day_num = 0
            weekday = day_name[day_num]

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
            'birthday': datetime(year=1996, month=8, day=3)
        },
        {
            'name': 'Ann',
            'birthday': datetime(year=1996, month=7, day=31)
        },
        {
            'name': 'Rich',
            'birthday': datetime(year=2022, month=7, day=29)
        },
    ]

    get_birthdays_per_week(users)