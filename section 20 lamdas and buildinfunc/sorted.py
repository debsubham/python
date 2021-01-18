####sorted  (works on anything that is iterable)

more_numbers = [6,8,1,6,9,4,3,7,2,1]
print(sorted(more_numbers)) ## [1, 1, 2, 3, 4, 6, 6, 7, 8, 9]  ##=>> not change the initial values serial
more_numbers.sort() ###output is same but change the values serial in more_numbers

print(sorted(more_numbers, reverse=True))


users = [{
        "name" : "Subham",
        "title" : "Deb",
        "address" : "amd",
        "count" : 19
    },
    {
        "name" : "Subham deb",
        "adderss" : "merua",
        "title" : "Deb",
        "count" : 12
    },
    {
        "name" : "Subham",
        "title" : "Deb",
        "address" : "amd",
        "count" : 55
    },
    {
        "name" : "Subham",
        "title" : "Deb sfgasdgasdg",
        "address" : "amdfgasgag",
        "count" : 8
    },
    {"name" : "Subham",
        "title" : "Deb",
        "address" : "Merua, Amadpur, Memari",
        "count" : 2}

]


print(sorted(users, key=len)) ##sort by length of dictionaries

print(sorted(users, key=lambda x : x["count"])) ## sorted by count key