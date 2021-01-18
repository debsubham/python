## max (string, dicts with same keys)

max([3,4,1,2])  ##4
max((1,2,3,4)) ##4
max('awesome') # "w"
max({1 : "a",3:"c", 2:"b"}) ##3

names = ["subham", "deb", "babai"]

max(len(name) for name in names) ##'subham' ##another methods below
max(names, key=lambda x: len(x) )

## (min) same things
