import re
from pprint import pprint


with open('../README.md', 'r', encoding="utf-8") as f:
    f = f.read()

lines = f.split('#### **_使用 five cross valid_**')[1].split('\n')

train_mae = {}
before_para_finding_mae = {}
after_para_finding_mae = {}

last_line = ''
for index, line in enumerate(lines):
    if last_line == '':

        name = re.sub(r'[>\\]', '', line).strip()
        for reader in lines[index:]:
            if reader == '':
                break

            match = re.search(r'(\d+)', reader)
            if match:
                number = int(match.group(1))
                cleaned_string = re.sub(r'[^a-zA-Z ]', '', reader).strip()
                if cleaned_string == 'train mae':
                    train_mae[name] = number
                elif cleaned_string == 'before para finding mae':
                    before_para_finding_mae[name] = number
                elif cleaned_string == 'after para finding mae':
                    after_para_finding_mae[name] = number

    last_line = line


# pprint(train_mae)
# pprint(before_para_finding_mae)
# pprint(after_para_finding_mae)

print(sorted(train_mae.items(), key=lambda x: x[1]))
print(sorted(before_para_finding_mae.items(), key=lambda x: x[1]))
print(sorted(after_para_finding_mae.items(), key=lambda x: x[1]))