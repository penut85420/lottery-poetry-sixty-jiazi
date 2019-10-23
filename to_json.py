import os
import re
import yaml
import json

p = re.compile('(\d+)')

dataset = [i for i in range(60)]
for dir_path, _, file_list in os.walk('./resources'):
    for file_name in file_list:
        full_path = os.path.join(dir_path, file_name)
        with open(full_path, 'r', encoding='UTF-8') as fin:
            data = yaml.load(fin, Loader=yaml.BaseLoader)
        fid = int(p.findall(full_path)[0]) - 1
        dataset[fid] = data

with open('sixty_jiazi.json', 'w', encoding='UTF-8') as fout:
    json.dump(dataset, fout, ensure_ascii=False, indent=2)
