from github import Github
import sys
import pandas
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from scipy import stats

DEFAULT_MAX_ROWS = 10
REPO_FOLL_COLUMNS = 2
FOLL_NODE_LISTS = 2

class repoFollowers:

    def __init__(self, username, g, rows, clean):
        self.username = username
        self.g = g
        self.prev = []
        self.df = pandas.DataFrame(columns=['Repos', 'Followers'])
        self.currentPerc = 0
        self.rows = rows
        self.clean = clean

    def returnDf(self):
        if self.clean:
            print("test")
            self.cleanData()
        return self.df


    def cleanData(self):
        q1 = self.df['Followers'].quantile(0.25)
        q3 = self.df['Followers'].quantile(0.75)
        iqr = q3 - q1
        fence_low = q1-1.5*iqr
        fence_high = q3+1.5*iqr
        self.df = self.df.loc[(self.df['Followers'] > fence_low) & (self.df['Followers'] < fence_high)]

    def inter(self):
        currentUser = self.g.get_user(self.username)
        self.prev.append(currentUser.login)
        self.df = self.df.append({'Repos' : currentUser.public_repos, 'Followers' : currentUser.followers}, ignore_index = True)
        if (self.df.size >= self.rows * REPO_FOLL_COLUMNS):
            return True

        named_followers = currentUser.get_followers()
        if named_followers is None:
            return False

        if ((100 * self.df.size)/(self.rows * REPO_FOLL_COLUMNS)>=(self.currentPerc + 10)):
            self.currentPerc = self.currentPerc + 10
            print('{}% complete'.format(self.currentPerc))

        for i in named_followers:
            if (self.df.size >= self.rows * REPO_FOLL_COLUMNS):
                return True
            if i.login not in self.prev:
                nextFollower = str(i.login)
                self.username = nextFollower
                if (self.inter()):
                    return True
        return False


class followersNetwork():
    def __init__(self, username, g, rows):
        self.username = username
        self.g = g
        self.prev = []
        self.a = []
        self.b = []
        self.currentPerc = 0
        self.rows = rows

    def returnG(self):
        self.df = pandas.DataFrame({ 'from':self.a, 'to':self.b})
        graph = nx.from_pandas_edgelist(self.df, 'from', 'to')
        return graph

    def inter(self):
        currentUser = self.g.get_user(self.username)
        self.prev.append(currentUser.login)
        if (len(self.a) >= self.rows * FOLL_NODE_LISTS):
            return True

        named_followers = currentUser.get_followers()
        if named_followers is None:
            return False



        for i in named_followers:
            if (len(self.a) >= self.rows):
                return True
            if ((100 * (len(self.a)))/(self.rows)>=(self.currentPerc + 10)):
                self.currentPerc = self.currentPerc + 10
                print('{}% complete'.format(self.currentPerc))
            if i.login not in self.prev:
                nextFollower = str(i.login)
                self.a.append(currentUser.login)
                self.b.append(nextFollower)

        for i in named_followers:
            if (len(self.a) >= self.rows):
                return True
            if i.login not in self.prev:
                nextFollower = str(i.login)
                self.username = nextFollower
                if (self.inter()):
                    return True
        return False


successfulLogin = False
for attempts in range(10):
    if not successfulLogin:
        try:
            token = input('Input your access token to begin--> ')
            g = Github(str(token))
            user = g.get_user()
            print("Hello {}, use the following commands to interrogate".format(user.name),
                "the Github API and display the data. Type 'quit' to stop the program.",
                "\n\n-Followers vs Repos Graph:",
                "\nfr <row_size> <clean>",
                "\n\n-Followers Network Graph",
                "\nfg <row_size>")
        except:
            print("Error: Bad Credentials. You inputted '{}'".format(str(token)))
        else:
            successfulLogin = True
            for x in sys.stdin:
                args = x.split(" ")

                if len(args) == 1:
                    if args[0] == "fr\n":
                        args[0] = "fr"
                    elif args[0] == "fg\n":
                        args[0] = "fg"
                    args.append(DEFAULT_MAX_ROWS)

                if len(args) == 0:
                    print("You must input something!")

                if args[0] == "quit\n" or args[0].lower() == "exit\n":
                    print("Stopping program.")
                    break
                elif args[0] == "fr":
                    clean = False
                    if len(args) == 3:
                        if args[2] == "-cl\n":
                            clean = True
                    p = repoFollowers(user.login,g,int(args[1]),clean)
                    p.inter()
                    df = p.returnDf()
                    df.plot(x='Repos', y='Followers', style='o')
                    plt.show()
                elif args[0] == 'fg':
                    p = followersNetwork(user.login,g, int(args[1]))
                    p.inter()
                    g = p.returnG()
                    nx.draw(g, with_labels=True)
                    plt.show()
                else:
                     print("Error: command not found.")

if not successfulLogin:
    print("Too many login attempts. Stopping program.")
