
minutes=42
seconds=42
TotalSeconds= minutes*60 +seconds
TotalHours=TotalSeconds/3600
kilometers=10
miles=kilometers*1.61

pace=(TotalSeconds/60)/miles
print('Pace=',pace, 'minutes/mile')

print('Avg Speed=', miles/TotalHours, 'MPH')