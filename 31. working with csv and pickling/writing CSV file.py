from csv import writer
with open("cars.csv" ,"w") as file:
  csv_writer = writer(file)
  csv_writer.writerow(["Name", "Color"])
  csv_writer.writerow(["Super Splender", "Red"])
  csv_writer.writerow(["Bmw", "Blue White"])