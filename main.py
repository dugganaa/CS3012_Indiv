from github import Github

username = input('username --> ')
password = input('password --> ')

g = Github(str(username), str(password))
user = g.get_user()

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
