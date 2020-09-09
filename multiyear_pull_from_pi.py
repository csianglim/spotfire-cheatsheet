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


for year in range(2010,2021):
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
