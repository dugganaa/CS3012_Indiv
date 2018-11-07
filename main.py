from github import Github

g = Github("dugganaa","not_Actually_my_password")
for repo in g.get_user().get_repos():
    print(repo.name)


