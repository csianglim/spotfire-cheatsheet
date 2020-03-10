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

## Read values from a data table column using IronPython
```
# import the DataValueCursor class
from Spotfire.Dxp.Data import DataValueCursor

# set up the data table reference
dt = Document.Data.Tables["Data Table"]
# set up the column reference
col = DataValueCursor.CreateFormatted(dt.Columns["col"])

# move the cursor to the first row of the column
# (GetRows() returns an iterable, and next() advances it to the first result)
dt.GetRows(col).next()

# update the document property
Document.Properties["B"] = col.CurrentValue
```

https://stackoverflow.com/questions/49020596/update-property-control-value-using-another-property-control-spotfire
