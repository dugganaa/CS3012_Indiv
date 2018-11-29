from github import Github
import pandas
import numpy as np
import matplotlib.pyplot as plt





MAX_ROWS = 10
REPO_FOLL_COLUMNS = 2

class repoFollowers:


    def __init__(self, username, g):
        self.username = username
        self.g = g
        self.prev = []
        self.df = pandas.DataFrame(columns=['Repos', 'Followers'])
        self.currentPerc = 0

    def returnDf(self):
        return self.df

    def inter(self):
        currentUser = self.g.get_user(self.username)
        self.prev.append(currentUser.login)
        self.df = self.df.append({'Repos' : currentUser.public_repos, 'Followers' : currentUser.followers}, ignore_index = True)
        if (self.df.size >= MAX_ROWS * REPO_FOLL_COLUMNS):
            return True

        named_followers = currentUser.get_followers()
        if named_followers is None:
            return False

        if ((100 * self.df.size)/(MAX_ROWS * REPO_FOLL_COLUMNS)>=(self.currentPerc + 10)):
            self.currentPerc = self.currentPerc + 10
            print('{}% complete'.format(self.currentPerc))

        for i in named_followers:
            if (self.df.size >= MAX_ROWS * REPO_FOLL_COLUMNS):
                return True
            if i.login not in self.prev:
                nextFollower = str(i.login)
                self.username = nextFollower
                if (self.inter()):
                    return True
        return False


token = input('access token --> ')
g = Github(str(token))
user = g.get_user()

plot1 = repoFollowers(user.login, g)
plot1.inter()
dataframe1 = plot1.returnDf()
dataframe1.plot(x='Repos', y='Followers', style='o')
plt.show()
print(dataframe1)
