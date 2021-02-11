# all syntax use in console


file = open("./story.txt")
file.read()

file.seek(1) #use for read file again from curser 0
file close()
file.closed ###for checking


##with
with open("story.txt") as f:
  data = f.read()

f.__enter__()
f.__exit__()
data ## is store the text of story.txt 