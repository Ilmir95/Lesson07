import os
pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, foldres in pattern.items():
   if os.path.exists(root):
      print(root, 'существует')
   else:
      for folder in foldres:
         cur_dir = os.path.join(root, folder)
         os.makedirs(cur_dir)
