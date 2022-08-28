import os
import json


src_dir = 'convos/'


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


if __name__ == '__main__':
    files = os.listdir(src_dir)
    data = list()
    for file in files:
        lines = open_file(src_dir + file).splitlines()
        compact = [i for i in lines if len(i) > 1]
        if 'USER:' in compact[-1]:
            a = compact.pop(-1)
        if len(compact) > 0:
            completion = compact.pop(-1).replace('小方:', '')
        else:
            completion = compact
        print(file, lines[0])
        new = list()
        for i in compact:
            if 'User:' in i:
                new.append(i.lower().replace('user:', 'USER:').replace('.','').replace(',','').replace('!','').replace('?','').replace('"',''))
            else:
                new.append(i.replace('-',' ').replace('  ', ' '))
        prompt = '\n'.join(new) + '\小方:'
        info = {'prompt': prompt, 'completion': completion}
        data.append(info)
    with open('小方.jsonl', 'w') as outfile:
        for i in data:
            json.dump(i, outfile, ensure_ascii=False)
            outfile.write('\n')