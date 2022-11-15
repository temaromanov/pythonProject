storona_1 = float(input('введите сторону 1: '))
storona_2 = float(input('введите сторону 2: '))
storona_3 = float(input('введите сторону 3: '))

pol = (storona_1 + storona_2 + storona_3) / 2 # полупериметр

s = (pol * (pol - storona_1) * (pol - storona_2) * (pol - storona_3)) ** 0.5
print(s)
