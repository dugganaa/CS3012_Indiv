from github import Github
import pandas
import matplotlib.pyplot as plt

username = input('username --> ')
password = input('password --> ')

g = Github(str(username), str(password))

user = g.get_user()

try:
    print(user.name)
    print("Bio: " + str(user.bio))
    print("Number of collaborators: " + str(user.collaborators))
    print("Company name: " + str(user.company))
    print("Public Gists " + str(user.public_gists))
    print("Email: " + str(user.email))
    print("Followers: " + str(user.followers))
    print("Following: " + str(user.following))
    print("Hireable: " + str(user.hireable))
    print("ID: " + str(user.id))
    print("Public repos: " + str(user.public_repos))
    print("Private repos: " + str(user.total_private_repos))
except:
    print("Looks like those login details weren'te quite right..")

df = pandas.DataFrame({ 'collaborators' : int(user.collaborators),
                        'public_gists' : int(user.public_gists),
                        'followers' : int(user.followers),
                        'following' : int(user.following),
                        'public_repos' : int(user.public_repos),
                        'private_repos' : int(user.total_private_repos)}, index=[0])
df.plot(kind='bar')
plt.show()
