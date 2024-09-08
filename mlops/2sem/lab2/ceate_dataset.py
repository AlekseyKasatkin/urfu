import pandas as pd
import requests
from tqdm import tqdm

import os

print("Текущая рабочая директория:", os.getcwd())

def getdata(offset=0, limit=100):
    link = (f"https://datasets-server.huggingface.co/rows?dataset=yashraizad%2Fyelp-open-dataset-users&config=default"
            f"&split=train&offset={offset}&length={limit}")
    r = requests.get(link)
    data_dict = r.json()
    rows_dict = [row['row'] for row in data_dict["rows"]]
    df = pd.DataFrame(rows_dict)
    # print(f"Was there {len(df)} rows?")

    return df


for i in tqdm(range(10)):
    offset = i * 100
    df_tmp = getdata(offset=offset)
    if i == 0:
        df = df_tmp
    else:
        df = pd.concat([df, df_tmp]).reset_index(drop=True)

project_dir = os.path.dirname(__file__)
df.to_pickle(os.path.join(project_dir, 'data.pkl'))