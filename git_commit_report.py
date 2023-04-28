# Import necessary modules
from git import Repo, InvalidGitRepositoryError
import os
import arrow

# repos path
path = "D:\Work"
folders = next(os.walk(path))[1]


def print_commits(repos):
    # Define the keywords used to classify the commits
    create_keywords = ['create', 'add', 'new']
    update_keywords = ['update', 'modify', 'change']
    bugfix_keywords = ['bug', 'fix', 'resolve']

    ignore_keywords = ['merge branch']
    try:
        repo = Repo(repos)
    except InvalidGitRepositoryError:
        print(repos+' is not a git repo, skipping')
        return
    # Open the Git repository
    # repo = Repo(repos)

    # Create a dictionary to store the commit classifications by author
    commit_dict = {}

    # Iterate through each commit and classify it based on the commit message
    for commit in repo.iter_commits():
        message = commit.message.lower()
        if any(keyword in message for keyword in ignore_keywords):
            continue

        if any(keyword in message for keyword in create_keywords):
            classification = 'Create'
        elif any(keyword in message for keyword in update_keywords):
            classification = 'Update'
        elif any(keyword in message for keyword in bugfix_keywords):
            classification = 'Bugfix'
        else:
            classification = 'Other'

        author = commit.author.name

        if author not in commit_dict:
            commit_dict[author] = {
                'Create': {'commits': [], 'count': 0},
                'Update': {'commits': [], 'count': 0},
                'Bugfix': {'commits': [], 'count': 0},
                'Other': {'commits': [], 'count': 0},
            }
            # commit_dict[author][classification] += 1
        date = arrow.get(commit.committed_datetime).humanize()
        commit_dict[author][classification]['count'] += 1
        commit_dict[author][classification]['commits'].append(
            date+'  '+message)

    repo_name = os.path.basename(repo.working_dir)
    with open('output/'+repo_name+'.txt', 'w') as f:
        for author, commit in commit_dict.items():
            f.write(f"{author}:\n")
            for clss, clsss in commit.items():
                f.write(f"\t{clss}({clsss['count']})\n")
                for messages in clsss['commits']:
                    f.write(f"\t\t{messages}")


for folder in folders:
    full_path = os.path.join(path, folder)
    # print(full_path)
    print_commits(full_path)


# Define the path to the Git repository
# repo_path = 'D:\Work\Fileserver'
# repo_path = 'D:\Work\laravel streaming'
