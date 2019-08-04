import requests
import json
import math
from lxml import html
from operator import itemgetter
from collections import Counter

fork_count = dict()
star_count = dict()
contributor_count = dict()
api_token = "113c9bcde00367ca47520b1ba820f3e755f0b222"


def handle(org):
    #step 1: get all repo data from /org/repos (paginated by 30)
    res = requests.get('https://api.github.com/orgs/' + org, headers={'Authorization': 'token %s' % api_token})
    org_info = res.json()
    numberOfRepos = org_info['public_repos']
    pages = math.ceil(int(numberOfRepos) / 30)
    processRepos(pages, org)

    most_fork = dict(Counter(fork_count).most_common(5))
    most_star = dict(Counter(star_count).most_common(5))

    most_fork_list = [(k, v) for k, v in most_fork.items()]
    most_star_list = [(k, v) for k, v in most_star.items()]

    sorted_most_fork_list = sorted(most_fork_list, key=itemgetter(1), reverse=True)
    sorted_most_star_list = sorted(most_star_list, key=itemgetter(1), reverse=True)

    return sorted_most_fork_list, sorted_most_star_list



def processRepos(pages, org):
    for x in range(pages+1):
        repo_info = createRequest(x, org)
        for repo in repo_info:
            fork_count[repo['name']] = repo['forks_count']
            star_count[repo['name']] = repo['stargazers_count']
            # contributor_count[repo['name']] = getTotalNumberOfContributors(org, str(repo['name']))





def createRequest(pageNumber, org):
    res = requests.get('https://api.github.com/orgs/' + org + "/repos?page=" + str(pageNumber), headers={'Authorization': 'token %s' % api_token})
    repo_info = data = json.loads(res.text)
    return repo_info


##incomplete method - There was no great way to getting the number of contributors because github does not have an API that directly gives that number
##Option 1: Scrape the actual github url of the repo for the number - pretty slow and inefficient
##Option 2: Set results per page to 1 and then read the response header to see how many pages there are to get the total number of contributors - this approach would require to many calls to github's API
def getTotalNumberOfContributors(org, repoName):
    url = 'https://github.com/' + org + "/" + repoName
    print(url)
    r = requests.get('https://github.com/' + org + "/" + repoName )

    xpath = '//span[contains(@class, "num") and following-sibling::text()[normalize-space()="contributors"]]/text()'
    contributors_number = int(html.fromstring(r.text).xpath(xpath)[0].strip())
    print(contributors_number)
    return contributors_number


def printItems(dictObj, indent):
    print( '  '*indent + '<ul>\n' )
    for k,v in dictObj.iteritems():
        if isinstance(v, dict):
            print ('  '*indent , '<li>', k, ':', '</li>')
            printItems(v, indent+1)
        else:
            print( ' '*indent , '<li>', k, ':', v, '</li>')
    print ('  '*indent + '</ul>\n')