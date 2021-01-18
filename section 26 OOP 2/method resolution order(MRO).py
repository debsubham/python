##its helping in multiple inheritance calling

class A:
  def __init__(self):
    print("from A")

class B:
  def __init__(self):
    print("from B")

class C:
  def __init__(self):
    print("from C")

class D:
  def __init__(self):
    print("from D")

####using __mro__ to look the tree of inheritance
