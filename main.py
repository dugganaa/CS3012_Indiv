from github import Github
import pandas
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import Imputer

MAX_ROWS = 25
REPO_FOLL_COLUMNS = 2

token = input('access token --> ')
g = Github(str(token))
user = g.get_user()
followers = user.get_followers()

df = pandas.DataFrame(columns=['Repos', 'Followers'])
currentPerc = 0

def repoFoll(username, prev):
    currentUser = g.get_user(username)
    prev.append(currentUser.login)

    global df
    df = df.append({'Repos' : currentUser.public_repos, 'Followers' : currentUser.followers}, ignore_index = True)

    if (df.size >= MAX_ROWS * REPO_FOLL_COLUMNS):
        return True

    named_followers = currentUser.get_followers()
    if named_followers is None:
        return False

    global currentPerc
    if ((100 * df.size)/(MAX_ROWS * REPO_FOLL_COLUMNS)>=(currentPerc + 10)):
        currentPerc = currentPerc + 10
        print('{}% complete'.format(currentPerc))


    for i in named_followers:
        if (df.size >= MAX_ROWS * REPO_FOLL_COLUMNS):
            return True
        if i.login not in prev:
            nextFollower = str(i.login)
            if (repoFoll(nextFollower, prev)):
                return True
    return False

print("Interrogating API, this may take a few seconds...")
repoFoll(username = user.login, prev = [])
print(df)

df.plot(x='Repos', y='Followers', style= 'o')
plt.show()
