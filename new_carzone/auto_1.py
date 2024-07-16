import os
import shutil

THE_FILE_PATH=os.path.dirname(os.path.realpath(__file__))

print("\n\nthe file path is in "+str(THE_FILE_PATH)+"\n\n")

for file_model in os.listdir(THE_FILE_PATH):

      print(f"\n{str(file_model)}\n")
      if file_model.endswith(".py"):print("python file found")


#os.makedirs('/g3/g2/g1')

for x in dir(os):
      print(str(x))



list_the_files=os.system("dir C:\web\ new_carzone")
print(str(list_the_files))