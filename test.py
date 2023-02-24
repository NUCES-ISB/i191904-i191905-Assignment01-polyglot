from base import Sequence

def test_getText():
  obj=Sequence("Hello")
  assert obj.text()=="Hello"
