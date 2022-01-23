import os 
from tqdm import tqdm

def add_path(path, file_list):
    if os.path.isfile(path) and path[-5:] == '.java':
        file_list.append(os.path.join(path))
    elif os.path.isdir(path):
        dir_list = os.listdir(path)
        for dir in dir_list:
            add_path(os.path.join(path, dir), file_list)

    
if __name__ == '__main__':
    
    path = os.getcwd()
    dir_list = os.listdir(path)
    file_list = []
    for dir in tqdm(dir_list):
        add_path(os.path.join(path,dir), file_list)

    with open('javafilename.txt','w',encoding='utf-8') as fp:
        for i, file_name in enumerate(file_list):
            fp.write(str(i) + ',' + file_name + '\n')