
import requests
import pandas as pd

link = ("https://datasets-server.huggingface.co/rows?dataset=yashraizad%2Fyelp-open-dataset-users&config=default&split="
        "train&offset=0&length=100")
r = requests.get(link)
r.raise_for_status()
r.raw.decode_content = True
pd.DataFrame(r.json()['rows'])