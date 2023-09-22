import os
print('input container id:')
cid = input()
print('input save_name : ')
save_name = input()
os.system('sudo docker commit {} {}'.format(cid, save_name))
os.system('sudo docker login')
os.system('sudo docker push {}'.format(save_name))
