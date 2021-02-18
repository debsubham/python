## BAd method

# with open("fighter.csv") as file:
#   file.read()

#using reader
from csv import reader

with open("fighters.csv") as file:
  csv_reader = reader(file)
  for row in csv_reader:
    print(row)


# upper one is reader
# below one is DictReader
from csv import DictReader
with open("fighters.csv") as file:
  csv_reader = DictReader(file)
  print(csv_reader) 
  for row in csv_reader:
    print(f"{row} =>>>Name::: {row['Name']}, Country::: {row['Country']} \n\n")