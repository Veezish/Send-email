import yagmail
import os
from time import time, sleep

while True:
  sleep(60 - time()%60)
  sender = "testm0410@gmail.com"
  receiver = "vdoztlik@sharklasers.com"

  subjects = "LOL"

  content = """
  LOL contents
  """
  yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD2"))
  yag.send(to=receiver, subject=subjects, contents=content)
  print("Email sent")