with open("errors.txt", "w", encoding="utf-8") as filew:
    with open("logs.txt", "r", encoding="utf-8") as file:
        cnt=0
        for line in file:
            if line[0]=='E':
                filew.write(line)
                cnt+=1
        filew.write(f"Кількість критичних помилок: {cnt}")

