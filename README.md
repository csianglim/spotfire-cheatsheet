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
