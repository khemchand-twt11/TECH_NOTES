# print fibonacci series

n = 7;
series = [0,1]

for i in range(2,n):
    series.append(series[len(series)-1]+series[len(series)-2])

print(series)