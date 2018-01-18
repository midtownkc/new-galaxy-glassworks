import os

path =  os.getcwd()
files = os.listdir(path)
i = 0



for file in files:
    filename, file_extension = os.path.splitext("%s%s" os.getcwd(), file)
    if file_extension.lower() == jpg:
      i = i + 1
      os.rename(file, str(i))
