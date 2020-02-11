# spotfire-cheatsheet
Cheatsheet for Spotfire OVER expressions

## Difference between rows
```
[ColName] - Last([ColName]) OVER Previous([Axis.X])
```
## Timespan in Minutes Per Tag
```
TotalMinutes([Timestamp] - Min([Timestamp]) OVER (AllPrevious([Tag Name])))
```
