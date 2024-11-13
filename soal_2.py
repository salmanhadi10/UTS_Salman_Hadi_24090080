tahun = int(input("MASUKAN TAHUN :"))
if tahun %400 == 0 :
    print(f"{tahun} adalah tahun kabisat.")
elif tahun %4 == 0 and tahun % 100 != 0:
    print(f"{tahun} adalah tahun kabisat.")
else :
    print (f"{tahun}bukan tahun kabisat.")