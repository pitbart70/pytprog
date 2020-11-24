sek = int(input('Vvedite vremya v sekyndah \n'))

a,b = (divmod(sek,60))
print(a,b)
print()
ch=sek//3600
min=(sek-3600*ch)//60
s = sek - (3600*ch) - min*60
print(f'{ch}:{min}:{s}')