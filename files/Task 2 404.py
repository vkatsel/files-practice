with open("suspicious_requests.txt", "w", encoding="utf-8") as file:
    with open("server_logs.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.count("404 Not Found")!=0:
                file.write(line)
    #У файлі лише 4 помилки 404, а не 5 як сказано на сайті