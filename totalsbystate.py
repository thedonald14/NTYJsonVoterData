import glob
from analyzestatevotes import loadstatejson
import pandas as pd

def tallynyttotals():
    """This Function reviews all NYT JSON Voter Data and returns a SUM of all alleged Votes"""
    
    allstates = []
    for state in glob.glob('*.json'):
        statedf = loadstatejson(state)
        statename = state.split('.')[0]
        trumpvotes = sum([int(it) for it in statedf.new_trumpvotes])
        bidenvotes = sum([int(it) for it in statedf.new_bidenvotes])
        dictsum = {trumpvotes:'Trump',bidenvotes:'Biden'}
        winner = dictsum.get(max(dictsum))
        
        outcomes = {'State':statename,'TrumpTotal':trumpvotes, 'BidenTotal':bidenvotes, 'Leader': winner}
        allstates.append(outcomes)
    
    df = pd.DataFrame(allstates).set_index('State')
    df['Difference'] = df.TrumpTotal - df.BidenTotal
    df = df.sort_values(by=['Leader'],ascending=False)

    return df
 
if __name__ == '__main__':
    tallynyttotals()

# This is a Production of the Patriotic Deep State
# MAGA
# print(f"{chr(21328)}")
