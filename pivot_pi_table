from Spotfire.Dxp.Data import DataFlowBuilder, DataColumnSignature, DataType, DataSourcePromptMode
from Spotfire.Dxp.Data.Transformations import PivotTransformation
from System.Collections.Generic import List
from Spotfire.Dxp.Data.Import import DataTableDataSource
from Spotfire.Dxp.Data.Transformations import ColumnAggregation

table = Document.Data.Tables['Data_Merged']

ds = DataTableDataSource(table)
ds.IsPromptingAllowed = False
ds.ReuseSettingsWithoutPrompting = True
dfb = DataFlowBuilder(ds, Application.ImportContext)
pivot = PivotTransformation()

# Identity column
list = List[DataColumnSignature]()
list.Clear()
col = table.Columns['Timestamp']
list.Add(DataColumnSignature(col))
pivot.IdentityColumns = list

# Value columns.
list2 = List[ColumnAggregation]()
list2.Clear()
col = table.Columns['Numeric Value']
colAg = ColumnAggregation(DataColumnSignature(col),'None')
list2.Add(colAg)
pivot.ValueColumns = list2

# Category columns
list3 = List[DataColumnSignature]()
list3.Clear()
col = table.Columns['Tag Name']
list3.Add(DataColumnSignature(col))
pivot.CategoryColumns = list3
pivot.ResultNamingExpression = "%C"

# Build pivot
dfb.AddTransformation(pivot)
flow = dfb.Build()
pivot_table_name = "Data_Merged_Pivoted"

def getDataTable(tableName):
    try:
        return Document.Data.Tables[tableName]
    except:
        print ("Cannot find data table: " + tableName + ". Returning None")
        return None

dt = getDataTable(pivot_table_name)
if dt != None:
    #If exists, replace it
    dt.ReplaceData(flow)
else:
    #If it does not exist, create new
    Document.Data.Tables.Add(pivot_table_name, flow)
