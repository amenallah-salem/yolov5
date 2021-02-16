import os

def dump_xml():
  list_dir_files= os.listdir(os.chdir('./images/'))
  for x in range(len(list_dir_files)):
    for file_name in os.listdir(os.path.join(os.getcwd(), list_dir_files[x])):
      if file_name.endswith('.xml'):
        os.remove(os.path.join(os.getcwd() +'/'+ list_dir_files[x] ,file_name))
      else:
        pass 
  print('Finished removing xml files successfuly')
  print('current dir:', os.getcwd())

if __name__="__main__":
  dump_xml()
