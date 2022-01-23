seconds = int(input())
minute = seconds // 60
seconds= seconds % 60
hour = minute // 60
minute = minute % 60
print(f'{hour}:{minute}:{seconds}')

