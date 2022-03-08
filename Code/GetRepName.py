import time
from urllib.request import urlopen
from urllib.request import Request
import json


def get_results(search, headers, page, stars):
    url = 'https://api.github.com/search/repositories?q={search}%20&page={num}&per_page=100&sort=stars' \
          '&order=desc'.format(search=search, num=page)    
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = json.loads(response.decode())
    return result


if __name__ == '__main__':
    # Specify Java Repository
    search = 'language:java'

    # Modify the GitHub token value
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': 'token ************************************',
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }

    count = 1
    stars = 0
    repos_list = []
    stars_list = []
    for page in range(1, 11):
        results = get_results(search, headers, page, stars)
        for item in results['items']:
            repos_list.append([count, item["full_name"], item["clone_url"]])
            stars_list.append(item["stargazers_count"])
            count += 1
        print(len(repos_list))
    stars = stars_list[-1]
    print(stars)
    with open("./top1000Repos.txt", "a", encoding="utf-8") as f:
        for i in range(len(repos_list)):
            f.write(str(repos_list[i][0]) + "," + repos_list[i][1] + "," + repos_list[i][2] + "\n")
