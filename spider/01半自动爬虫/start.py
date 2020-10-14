import re
import csv

with open('source.txt', 'r') as f:
    source = f.read()


result_list = []
username_list = re.findall('"主题作者: (.*?)"', source, re.S)
title_list = re.findall('<div class="threadlist_abs threadlist_abs_onlyline ">(.*?)</div>', source, re.S)

print(username_list)
print(title_list)