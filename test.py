from polyglot.text import Word

def test_getString():
  obj=Word("Hello")
  assert str(obj)=="Hello"

def test_getString():
  obj=Word("ABC-1029[]{}")
  assert str(obj)=="ABC-1029[]{}"
  
def test_getString():
  obj=Word("123=-/.][,l")
  assert str(obj)=="123=-/.][,l"
