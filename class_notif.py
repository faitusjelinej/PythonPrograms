class notification(object):
  def __init__(self, user, message):
    self.user = user
    self.message = message
    self.item = []
  def send_message(self):
    print('Message sent to {} and the message is {}'.format(self.user, self.message))

  def change_user(self, user):
    self.user = user



J = notification('Jeline', 'Hi this is Jeline')
S = notification('Shoba', 'Hi this is Shoba')

J.send_message()
S.send_message()
S.change_user('Gia')
S.send_message()

print(J.item)
J.item.append('I like to play')

print(J.item)
print(S.item)
