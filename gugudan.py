print("구구단 몇 단을 계산할까요 : ")
user_input = input()
print("구구단 "+str(user_input)+"단을 계산합니다")
int_input = int(user_input)
for i in range(10):
    result = int_input*i
    print(user_input,"X",i,"=",result)

