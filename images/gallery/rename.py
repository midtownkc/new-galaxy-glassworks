import os

path =  os.getcwd()
files = os.listdir(path)
i = 0

for file in files:
    filename, file_extension = os.path.splitext(path + file)
    if file_extension.lower() == '.jpg':
      i = i + 1
      new_name = (str(i) + file_extension.lower())
      os.rename(file, new_name)