from genericpath import exists
import os
import errno
#creating folder and file inside that folder
filename = "C:\\Users\\845160\\Downloads\\Python\\13yearold\\multi0.txt"
print(filename)

if not os.path.exists(os.path.dirname(filename)):
        print(filename)
        try:
            os.makedirs(os.path.dirname(filename))

        except OSError as exc: # Guard against race condition
             if exc.errno != errno.EEXIST:
                 raise
       

for i in range(2,5):
            try:
             fo=open("C:\\Users\\845160\\Downloads\\Python\\13yearold\\multi{0}.txt".format(i),"w")
             for j in range(1,11):
                 fo.write("%d * %d = %d \n"%(i,j,i*j))
                 
        
            except OSError as exc: # Guard against race condition
             if exc.errno != errno.EEXIST:
                 raise
            fo.close()
   

       

        
        

print(os.listdir("C:\\Users\\845160\\Downloads\\Python\\13yearold"))
