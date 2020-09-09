# VALID UP TO 30s intervals. For more granularity use supermultiyear_pull_from_pi -> splits into quarterly data tables. valid up to 10s intervals

import  clr
clr.AddReference("SpotfirePS.Framework.OSIPIDataSource, Version=1.0.0.0,  \
          Culture=neutral, \
          PublicKeyToken=ef33e7f75d4ca16b")
#
# Import  the required  classes
#
from  SpotfirePS.Framework.OSIPIDataSource.DataSource.TagData import  DataSourcePromptModel
from  SpotfirePS.Framework.OSIPIDataSource.DataSource.TagData import  DataSourceImpl
from  SpotfirePS.Framework.OSIPIDataSource.DataSource.TagData import  OSIPIDataSourceTagLocator
from  SpotfirePS.Framework.OSIPIDataSource.DataSource.TagData import  TimeRange

year_start = 2010
year_end = 2021

for year in range(year_start,year_end):
	print("Working on year: {}".format(year))
	pm  = DataSourcePromptModel()
	timerange = TimeRange (
		   "01/01/{} 12:00:00 AM".format(year),      # Start Time
		   "01/01/{} 12:00:00 AM".format(year+1),         # End Time
		   ""           # Comment for this  TimeRange
	)

	for tag_name in ["sinusoid"]:
		tag  = OSIPIDataSourceTagLocator (
				"servername",             #  Server
				"",                      # UserName
				"",                      # Password
				"",                      # Domain
				"Windows",               # Authmode
				tag_name,              # TagName
				timerange,               # TimeRange
				100						 # NumPoints
		)
		pm.TagList.Add(tag)

	pm.RetrievalMode  = "Average"
	pm.CalculationBasis  = "Time Weighted"
	pm.SummaryDuration = "30s"
	pm.Timezone = "Local"

	ds  = DataSourceImpl(pm);
	dataTableName = "Data_" + str(year) 
	if  Document.Data.Tables.Contains(dataTableName):
	  Document.Data.Tables[dataTableName].ReplaceData(ds)
	else:
	  Document.Data.Tables.Add(dataTableName, ds)

# Merge into single data table
# Copyright © 2017. TIBCO Software Inc. Licensed under TIBCO BSD-style license.
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Data.Import import DataTableDataSource

#Define new table name
newTableName = 'Data_Merged'

#Define the source table
inputTableDS = DataTableDataSource(Document.Data.Tables["Data_" + str(year_start)])

#Function to return a Spotfire Data Table. Will return None if the data table does not exist
#parameter: tableName - the name of the data table in the Spotfire document
def getDataTable(tableName):
    try:
        return Document.Data.Tables[tableName]
    except:
        print ("Cannot find data table: " + tableName + ". Returning None")
        return None

#Check if new table already exists
dt = getDataTable(newTableName)
if dt != None:
    #If exists, replace it
    dt.ReplaceData(inputTableDS)
else:
    #If it does not exist, create new
    Document.Data.Tables.Add(newTableName, inputTableDS)

# The table where all other sources will be appended.
outputTable = Document.Data.Tables[newTableName]

for year in range(year_start,year_end):
	# Input Table Data Source, Add row settings to create new column and set values depending on sources, then append the new rows
	inputTableDS = DataTableDataSource(Document.Data.Tables["Data_" + str(year)])
	addRowsSettings = AddRowsSettings(outputTable, inputTableDS)
	outputTable.AddRows(inputTableDS, addRowsSettings)
