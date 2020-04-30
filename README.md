# spotfire-cheatsheet
Cheatsheet for Spotfire OVER expressions

## Difference between rows
```
[ColName] - Last([ColName]) OVER Previous([Axis.X])
```
https://community.tibco.com/questions/im-trying-calculate-difference-time-between-values-same-column-data-consecutive-rows

> This takes the current rows value in [myValue] and subtracts the [myValue] from the previous row (as determined by the [DateColumn] column). Note that an aggregation function is required for the OVER function, but since Previous() just returns a single row, the aggregation is irrelevant - Min(), Max(), Avg(), etc would all return the same original value.

## Count number of times character appears in a string
```
You can replace all occurrences of the character in your string and then compare the length of the trimmed string with the length of your original string:
Len([Column 1]) - Len(Substitute([Column 1],"C",""))
```
https://community.tibco.com/questions/how-can-i-count-number-times-letter-appears-string-so-example-i-have-string-aaaabcdddddcdd

## Timespan in Minutes Per Tag
```
TotalMinutes([Timestamp] - Min([Timestamp]) OVER (AllPrevious([Tag Name])))
```

## Create an ascending grouped index per timestamp for each group
```
Rank([Timestamp],[Group])
```

https://community.tibco.com/questions/number-records-and-difference-same-column-based-previous-row-value

> Yes, in the Rank() function just add as many different columns you need to group by:

Rank(RowId(),[Name], [mygroup1],[mygroup2])
But it sounds like you might want to order based on that date time. In that case you wouldn't rank the RowId(), but instead your date time column:

Rank([mydatetime],[Name])

## Get the latest timestamp over intersection of tag names and tag groups

```
Max([Timestamp]) OVER (Intersect([Tagname],[Group]))
```

https://stackoverflow.com/questions/43002866/spotfire-how-to-get-the-last-value-in-a-column

## Get the latest value of a group based on the timestamp

```
If([Timestamp]=Max([Timestamp]) OVER (Intersect([Tagname],[Group])),[Value])
```


## Calculate difference between row n and row n-1 n per group

```
[Value] - First([Value]) OVER (Intersect([Group],Previous([Grouped Index])))
```

## Calculate difference between row n and row n+1 per group

```
[Value] - First([Value]) OVER (Intersect([Group],Next([Grouped Index])))
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

## Trigger JS from dropdown property change
```
MutationObserver = window.MutationObserver || window.WebKitMutationObserver;

//this is the target element to monitor changes
//just put the span id here. You can remove next line and add a script param called targetDomId
var targetDomId = "dropDownDocProp"

//function when dropdown value changes
var myFunction = function(oldValue,newValue){
  alert("old value:["+oldValue+"]\nnew value:["+newValue+"]")
                //click on a actioncontrol with python script
}


//no need to change after this line.
var target = document.getElementById(targetDomId)

//callback is the function to trigger when target changes
var oldVal = target.innerText.trim()
var callback = function(mutations) {
 newVal=$('#'+targetDomId+' .ComboBoxTextDivContainer').text()
 if(newVal!=oldVal) myFunction(oldVal,newVal)
 oldVal = newVal;
}

//this is to glue these two together
var observer = new MutationObserver(callback);

var opts = {
    childList: true, 
    attributes: true, 
    characterData: true, 
    subtree: true
}

observer.observe(target,opts);
```
https://spotfired.blogspot.com/2017/09/trigger-javascript-from-dropdown-list.html

## TERR Pass Through
- Use TERR to pass rows and columns through from one table to another
- Crosshairs 
https://community.tibco.com/questions/there-anyway-replicate-cross-hairs-lines-move-and-update-marking
https://datashoptalk.com/terr-in-spotfire-passing-marked-data-through-to-another-table/

## IronPython Refresh Data with Progress Bars

```
import traceback
import sys
from Spotfire.Dxp.Framework.ApplicationModel import *
ps = Application.GetService[ProgressService]()

def execRefreshData():
	try:
		ps.CurrentProgress.ExecuteSubtask("Refreshing Data");
		Document.Data.Tables.ReloadAllData()
		proc.CurrentProgress.ExecuteSubtask("Refresh is Complete")
	except:
		traceback.print_exc()

ps.ExecuteWithProgress("Refreshing Data", "Collecting DMC data from PI...", execRefreshData)
```

https://community.tibco.com/wiki/how-add-progress-bar-and-cancellation-option-when-executing-ironpython-scripts-tibco-spotfire
