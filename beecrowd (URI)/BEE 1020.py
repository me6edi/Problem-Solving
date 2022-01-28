days = int(input())
years = days // 365
years_r = days % 365
month = years_r // 30
days  = years_r % 30
print(years,"ano(s)")
print(month,"mes(es)")
print(days,"dia(s)")