# filedata = open("c:\Temp\exam01.txt", "w")

# for i in range(1, 11):
#     data = "%d 데이터저장\n" %i 
#     filedata.write(data)
# 2   # data = "데이터저장\n"
#     # filedata.writelines(data)

# filedata.close()


filedata = open("c:\Temp\exam01.txt", "r")

while True:
    readdata = filedata.readline()
    if not readdata: break
    print(readdata)

filedata.close()

