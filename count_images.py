import os 

cur_path = os.getcwd()

def fileCount(folder):
    count = 0
    for filename in os.listdir(folder):
        if filename[0] != '.':
            count += 1
    return count

def folderCount(directory):
    image_count = {}
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isdir(path):
            path = path.split('/')[-1]
            if path[0] != '.':
                image_count[path] = fileCount(path)
    return image_count

char_dic = folderCount(cur_path)

for character in char_dic:
    if char_dic[character] < 100:
        print(character)