import tableauserverclient

SECRET_KEY = "secret key"

# TABLEAU_AUTH = tableauserverclient.TableauAuth('vnankani', 'Tiktik666!!1')
TABLEAU_AUTH = tableauserverclient.PersonalAccessTokenAuth(
    'ADD TOKEN NAME HERE',
    'ADD PERSONAL ACCESS TOKEN HERE',
    'SITE GOES HERE')

USERS_LIST = ["user1", "user2", "user3", "user4"] #Users who have the access to the dashboard
PASSWORD_LOGIN = "usersPassword"