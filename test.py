from polyglot.text import Word

def test_getString():
  obj=Word("Hello")
  assert str(obj)=="Hello"
