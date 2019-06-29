import sys
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

#  Update the users in this list.
#  Each tuple represents the username, password, and email of a user.
users = [
    # ('user_1', 'phgzHpXcnJ', 'user_1@example.com'),
    # ('user_2', 'ktMmqKcpJw', 'user_2@example.com'),
    ('klminsu' , '2015318724', '2015318724', '강민수', '전자전기공학부', '41', '7'),
]

for username, password, student_id, name, major, section, group in users:
    try:
        print('Creating user {0}.'.format(username))
        user = User.objects.create_user(username=username, student_id=student_id,
            name=name, major=major, section=section, group=group)
        user.set_password(password)
        user.save()

        assert authenticate(username=username, password=password)
        print('User {0} successfully created.'.format(username))

    except:
        print('There was a problem creating the user: {0}.  Error: {1}.' \
            .format(username, sys.exc_info()[1]))