import os
from termcolor import colored
import sys
 
t_g = ""
t_b = ""
file_count, dir_count = 0, 0
 
#Fonksion başlangıcı
def tree(directory):
    global t_g, t_b, file_count, dir_count
   
    ls = os.listdir(directory)
    for i in ls:
        path = os.path.join(directory, i)
        if os.path.isdir(path):
            t_b = t_g
            if i.startswith(".") == False:
                dir_count += 1
                print t_g+colored(i, 'red', attrs=['bold'])
                t_g += " "*len(i)
                
                tree(yol)
        else:
            print t_g+colored(i, 'blue')
            file_count += 1
    t_g = t_b
    t_b = ""
 
## Fonksiyon çağırılmıştır.
tree(sys.argv[1])
print "\nDirectory Count = %s File Count = %s\n" % (dir_count, file_count)
