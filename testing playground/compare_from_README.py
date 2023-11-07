import re
from pprint import pprint


with open('../README.md', 'r', encoding="utf-8") as f:
    f = f.read()

lines = f.split('#### **_使用 five cross valid_**')[1].split('\n')

train_mse = {}
before_para_finding_mse = {}
after_para_finding_mse = {}

last_line = ''
for index, line in enumerate(lines):
    if last_line == '':

        name = re.sub(r'[>\\]', '', line).strip()
        for reader in lines[index:]:
            if reader == '':
                break

            match = re.search(r'(\d+\.\d+)', reader)
            if match:
                number = float(match.group(1))
                cleaned_string = re.sub(r'[^a-zA-Z ]', '', reader).strip()
                if cleaned_string == 'train mse':
                    train_mse[name] = number
                elif cleaned_string == 'before para finding mse':
                    before_para_finding_mse[name] = number
                elif cleaned_string == 'after para finding mse':
                    after_para_finding_mse[name] = number

    last_line = line


pprint(train_mse)
pprint(before_para_finding_mse)
pprint(after_para_finding_mse)