import time as t
i = 1
while False:
    t.sleep(0.1)
    with open('File_'+str(i)+".txt", 'x') as f:
        i += 1
        print("file creato")
        
    