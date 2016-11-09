class DataStruct:
  def __init__(self, fileName):
    self.file = open(fileName, 'r')
 
  def readline(self):
    string = self.file.readline().rstrip()
    try:
        num = int(string)
    except ValueError:
        num = 0
    return(num)
   
  def __del__(self):
    self.file.close()