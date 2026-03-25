with open("logs.txt", "r", encoding="utf-8") as file:
    cnt=0
    for line in file:
        if line[0]=='E':
            print(line)
            cnt+=1
    print(f"Кількість критичних помилок: {cnt}")