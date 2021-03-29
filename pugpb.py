from typing import List
from github import Github
from collections import OrderedDict
from dotenv import load_dotenv
import os

load_dotenv()


def members_of(organizations: List[str]) -> OrderedDict:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    g = Github(GITHUB_TOKEN)

    members = OrderedDict()
    members_set = set()

    for organization in organizations:
        team = g.get_organization(organization)
        users = team.get_members()

        for user in users:
            name = user.name if user.name else user.login
            members_set.add((name, user.email, user.login))

    members_set = sorted(members_set)

    for member in members_set:
        members[member[0]] = {"email": member[1], "github": member[2]}

    return members
