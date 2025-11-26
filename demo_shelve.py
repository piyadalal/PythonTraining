import shelve

movies = {'eric': ['pulp fiction', 'forest gump', 'platoon'],
'bertwin': ['kill bill', 'hateful 8', 'the firm'],
'stephan': ['james bond', 'Bourne', 'batman'],
'donald': ['lotr','the hobbit', 'mission impossible']
}

tv_series = {'eric': ['outlander', 'fallout'],
'bertwin': ['star trek', 'cagney and Lacey'],
'stephan': ['walking dead', 'reacher']
}



books = { 'eric': 'Python for dummies',
'bertwin': 'Java for dummies',
'stephan': 'Etiquette in Saunas'
}

with shelve.open('movies.shelve') as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open('movies.shelve') as db:
    print(f"Eric favourite movie is {db['movies']['eric'][0]}")
    print(f"Bertwin favourite series is {db['tv_series']['bertwin'][0]}")
    print(f"Stephan's favourite book is {db['books']['stephan']}")
