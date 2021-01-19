
def make_song(how_much=99, what_is="soda"):
  
  
  i=how_much
  while i>=0:
    if(i==1):
      yield f"Only 1 bottle of {what_is} left!"
    elif(i>1):
      yield f"{i} bottles of {what_is} on the wall."
    else:
      yield f"No more {what_is}!"
    i-=1

default_song= make_song(3,"some")

print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))