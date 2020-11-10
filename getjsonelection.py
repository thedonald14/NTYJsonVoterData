import requests
import pandas as pd

def downloadvoterjson():
    """This Function downloads the JSON File for each State in the 2020 Election from the NYT """
    
    # Get all State Names from CSV
    stnames = pd.read_csv("https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv")
    statelist = [st for st in stnames.State]
    
    # Download a JSON for each State in State Names.
    for st in statelist:
        url = f"https://static01.nyt.com/elections-assets/2020/data/api/2020-11-03/race-page/{st}/president.json"
        r = requests.get(url, allow_redirects=True)
        open(f"{st}.json", "wb").write(r.content)
