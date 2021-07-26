from django.shortcuts import render
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.request import urlopen
import json
from rest_framework.permissions import AllowAny


# get today date and subtract days from it
def get_date(days_to_subtract):
    d = datetime.today() - timedelta(days=days_to_subtract)
    d = str(d)
    date = d.split()
    return date[0]


# get number of repositories using specific language
def get_number_of_repositories(language):
    url = 'https://api.github.com/search/repositories?q=language:' + language
    res = urlopen(url).read()
    res = json.loads(res)
    return res['total_count']


# get programming languages in repository by repo full name
def get_languages_in_repository(repo_name):
    url = 'https://api.github.com/repos/' + repo_name + '/languages'
    res = urlopen(url).read()
    return json.loads(res)


class RepositoryList(APIView):
    """
    List top 3 trending repositories in Github.
    """

    def get(self, request):
        # Get top 3 repositories
        api_url = 'https://api.github.com/search/repositories?q=created:>' + str(
            get_date(10)) + '&sort=stars&order=desc&per_page=3'
        data = urlopen(api_url).read()
        json_data = json.loads(data)
        result = []
        for repo in json_data["items"]:
            # Get programming languages in repositories
            repo_languages = get_languages_in_repository(str(repo["full_name"]))
            languages = {}
            for lang in repo_languages:
                # Get number of repositories using specific language
                languages[lang] = get_number_of_repositories(lang)
            result.append({
                "id": repo["id"],
                "name": repo["name"],
                "full_name": repo["full_name"],
                "html_url": repo["html_url"],
                "languages": languages
            })
        return Response(result)
