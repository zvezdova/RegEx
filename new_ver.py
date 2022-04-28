from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

import re

def clean_text(str_list):

  new_list = []
  for element in str_list:  
    element = ','.join(element)  
    pattern = r'(,,+)'
    element = re.sub(pattern, r',', element)
    pattern = r'(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})((\s+)(\W)?(доб.)(\s)(\d+)([^,])?)?'
    element = re.sub(pattern, r'+7(\2)\3-\4-\5\7\9\11', element)
    pattern = r'(\n[А-я]+)(\s+|.)([А-я]+)(\s|.)'
    element = re.sub(pattern, r'\1,\3,', element)
    new_list.append(element)
  return(new_list)

contacts_list = clean_text(contacts_list)
print(contacts_list)

def remove_dup(str_list):

    import re    

    first_word_list = []
    for element in str_list:
        line = str(element)        
        pattern = re.search(r'\w+', line)
        first_word_list.append(pattern.group(0))
    
    from collections import Counter
    
    dubes_list = [item for item, count in Counter(first_word_list).items() if count > 1]
    num_str_dubes = [i for i, x in enumerate(first_word_list) if first_word_list.count(x) > 1]

contacts_list = remove_dup(contacts_list)
print(contacts_list)
   




    


