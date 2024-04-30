# filedata = open("c:\Temp\exam01.txt", "w")

# for i in range(1, 11):
#     data = "%d 데이터저장\n" %i 
#     filedata.write(data)
# 2   # data = "데이터저장\n"
#     # filedata.writelines(data)

# filedata.close()


# filedata = open("c:\Temp\exam01.txt", "r")

# while True:
#     readdata = filedata.readline()
#     if not readdata: break
#     print(readdata)

# filedata.close()

# open은 사용이 끝나면 close를 해야하는데, 
# with 는 open 후에 영역이 끝나면 자동 close() 된다. 

# with open(r"c:\Users\yunsu\Desktop\data\pp_sc\31_git\exam01.txt", "r+", encoding="UTF-8") as filedata:
#     dataresult = filedata.readlines()
#     filedata.write("\n데이터저장")
#     for data in dataresult:
#         print(data)


# 기본제공 json 모듈

# import json 

# jsondata = {
#     'empname' : '홍길동',
#     'empage' : 20 
# }

# with open("empdata.json", "w", encoding="utf-8") as filedata:
#     json.dump(jsondata, filedata, indent= '\t', ensure_ascii=False)


import json

jsondata = {
    'empname': '홍길동',
    'empage': 20 
}

# 쓰기 
with open("empdata24.json", "w", encoding="utf-8") as filedata:
    json.dump(jsondata, filedata, indent="\t", ensure_ascii=False)

# 파일에 데이터를 쓴 후에 다시 읽어와서 출력합니다.
with open("empdata24.json", "r", encoding="utf-8") as filedata:
    loaded_data = json.load(filedata)
    print(json.dumps(loaded_data, indent="\t", ensure_ascii=False))
