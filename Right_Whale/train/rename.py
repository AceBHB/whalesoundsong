import os
i = 1
while i < 30000:
    os.rename("train"+str(i)+".aiff", "rightwhale"+str(i)+".aiff")
    print("train"+str(i)+".aiff")
    i += 1

