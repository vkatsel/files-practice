
def inp_file():
    f_name, copy_f_name = map(str, input().split())
    try:
        with open(copy_f_name, "w", encoding="utf-8") as filew:
            with open(f_name,'r', encoding="utf-8") as filer:
                for line in filer:
                    filew.write(line)
    except FileNotFoundError:
        print("Йой, не можемо знайти цей файл! спробуйте ще раз")
        inp_file()
inp_file()