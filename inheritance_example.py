class Process(object):
  def __init__(self):
    print("Init Process")

  def process_function(self):
    return "process function"

class Client(Process):
  def __init__(self):
    print("Init Client")

  def process_function(self):
      return "client function"

class Server(Process):
  def __init__(self):
     print("Init Server")

  def process_function(self):
     result = super(Server, self).process_function()
     return result + ", Server function"

p = Process()
c = Client()
s = Server()

processes = [p,c,s]
print()
for m in processes:
    print(m.process_function())
