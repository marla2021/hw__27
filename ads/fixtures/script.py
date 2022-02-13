import json

import pandas

data_cat=pandas.read_csv("/Users/marinalarutina/PycharmProjects/hw__27/data/categories.csv",sep=",", encoding='utf-8').to_json()
data_ad=pandas.read_csv("/Users/marinalarutina/PycharmProjects/hw__27/data/ads.csv", sep=",").to_json()
with open("/Users/marinalarutina/PycharmProjects/hw__27/fixtures/ads/data_c.json", "w", encoding='utf-8') as write_file:
    json.dump(data_cat, write_file,ensure_ascii=False)

print(data_cat)