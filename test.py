import sys
import pandas as pd
import numpy as np
from timeit import default_timer as timer

def makedata(df,arities):
    '''

    Returns:
     pandas.DataFrame: The data
    '''

    for i, (name, data) in enumerate(df.items()):
        # ensure correct categories are recorded even if not
        # all observed in data
        df[name] = pd.Categorical(data,categories=range(arities[i]))
    return df


fobj = open(sys.argv[1])
variables = fobj.readline().rstrip().split()
arities = fobj.readline().rstrip().split()
arities = [int(x) for x in arities]
print(variables)
print(arities)
fobj.close()

df = pd.read_table(sys.argv[1],sep=' ',skiprows=1, dtype=int, header=0, names=variables)
df = makedata(df,arities)

begin = timer()
df.groupby(['A','B','D','F']).count()
end = timer()

print(df.groupby(['A','B','D','F']).count())

print("the time to get contab(A,B,D,F) used pandas")
print(end-begin)

