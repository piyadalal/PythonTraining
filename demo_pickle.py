#Description : This script will demo howto open for reading writing appending to text or
# #binary files using builtin open() funciton

import pickle
import pprint

movies =  {'eric': ['pulp fiction', 'forest gump', 'platoon'],
'bertwin': ['kill bill', 'hateful 8', 'the firm'],
'stephan': ['james bond', 'Bourne', 'batman']
 }

#open file handle for WRITING in BYTES mode for PICKLE
with open('movies.p', mode='wb') as fh_out: #<_io.TextIOWrapper name='movies.txt' mode='wt' encoding='UTF-8'>
    pickle.dump(movies, fh_out, protocol=0) # 0 - ascii 1-5: binary

with open('movies.p', mode='rb') as fh_in: #<_io.TextIOWrapper name='movies.txt' mode='wt' encoding='UTF-8'>
    pickle.load(fh_in)

pprint.pprint(movies)

import pickle, gzip

with gzip.open("data.pkl.gz", "wb") as f:
    pickle.dump(movies, f, protocol=pickle.HIGHEST_PROTOCOL)

# Reading
with gzip.open("data.pkl.gz", "rb") as f:
    data = pickle.load(f)


fh_out.close() # flushes buffers and closes the file handle
