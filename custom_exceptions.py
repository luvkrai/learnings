
class myexception(Exception):
  def __init__(self, message, errors):
    super().__init__(message)
    self.errors = errors

try:
  raise myexception("hello","my error")
except myexception as e:
  print(e)
  print(e.errors)