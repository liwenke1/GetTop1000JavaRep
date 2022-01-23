import git
import os
from tqdm import tqdm

if __name__ == '__main__':
    UrlFileName = 'top1000Repos.txt'
    with open(UrlFileName, 'r', encoding='utf-8') as fp:
        rep_list = fp.readlines()
        for rep in tqdm(rep_list):
            path = rep.split(',')[1].replace('/','@').strip()
            if os.path.exists(path):
                continue
            url = rep.split(',')[2].strip()
            git.Repo.clone_from(url,path)