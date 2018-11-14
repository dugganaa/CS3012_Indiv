from github import Github
import pandas as pd

MAX_ROWS = 200;

username = input('username --> ')
password = input('password --> ')

g = Github(str(username), str(password))
contFollDf = pd.dataframe(data = contFollData, columns=['Contributors', 'Followers'])

user = g.get_user()


'''
print(user.name)
print("Bio: " + str(user.bio))
print("Number of collaborators: " + str(user.collaborators))
print("Company name: " + str(user.company))
print("Number of contributions: " + str(user.contributions))
print("Email: " + str(user.email))
print("Followers: " + str(user.followers))
print("Following: " + str(user.following))
print("Hireable: " + str(user.hireable))
print("ID: " + str(user.id))
print("Public repos: " + str(user.public_repos))
print("Private repos: " + str(user.total_private_repos))
'''
followers = user.get_followers()
print(followers[0].login)
columns = 2

contFoll(user.login)

def contFoll(username):
    currentUser = Github(username)
    
    if (contFollDf.size() >= MAX_ROWS*columns):
        return
    
    totalFollowers = currentUser.followers
    totalContributions = currentUser.contributions
    
    contFollDf = contFollDf.append({'Contributors' : totalContributors}, {'Followers' : totalFollowers}, ignore_index=True)
    named_followers = currentUser.get_followers()
    if (named_followers == None):
        return
    
    i = 0
    while (contFollDf.size() <= MAX_ROWS * columns and i < named_followers.size()):
        nextFollower = str(currentUser.named_Followers[i].login)
        contFoll(nextFollower)
        i = i + 1
    
    

