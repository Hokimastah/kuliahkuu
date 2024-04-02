import datetime
a = int(input())
b = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

print(b[datetime.datetime(a-1,12,31).weekday()])