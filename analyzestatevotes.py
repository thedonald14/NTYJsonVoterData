import json
import pandas as pd
import dateutil.parser as dparser

def loadstatejson(statefile):
    """This Function loads JSON voting Data from local file into a DataFrame"""

    f = open(statefile)
    data = json.load(f)

    # Generate a List of Dicts
    dataone = data['data']['races'][0]['timeseries']
    df = pd.DataFrame(dataone)

    def gettrump(voteshares):
        return voteshares['trumpd']
    def getbiden(voteshares):
        return voteshares['bidenj']
    def returndatetime(datestr):
        return dparser.parse(datestr)
    
    
    df['trump_share'] = df.vote_shares.apply(gettrump)
    df['biden_share'] = df.vote_shares.apply(getbiden)
    df['timestamp'] = df.timestamp.apply(returndatetime)
    df['votechange'] = df['votes'].shift(-1) - df['votes']
    df['votechange'] = df['votechange'].shift(1)
    df['new_trumpvotes'] = df.trump_share*df.votechange
    df['new_bidenvotes'] = df.biden_share*df.votechange

    df = df.filter(items=['timestamp', 'votechange', 'trump_share', 'biden_share', 'new_trumpvotes','new_bidenvotes','votes','eevp_source','eevp'])

    return df
