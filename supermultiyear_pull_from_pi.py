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


for year in range(2010,2011):
  for quarter in [1,2,3,4]:
    print("Working on year: {}, {} half".format(year, quarter))
    pm  = DataSourcePromptModel()

    quarter_starts = ["01/01/{} 12:00:00 AM".format(year),
                      "04/01/{} 12:00:00 AM".format(year),
                      "07/01/{} 12:00:00 AM".format(year),
                      "10/01/{} 12:00:00 AM".format(year)]

    quarter_ends = ["04/01/{} 12:00:00 AM".format(year),
                      "07/01/{} 12:00:00 AM".format(year),
                      "10/01/{} 12:00:00 AM".format(year),
                      "01/01/{} 12:00:00 AM".format(year+1)]
              

    timerange = TimeRange (
         quarter_starts[quarter-1],      # Start Time
         quarter_ends[quarter-1],         # End Time
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
          100            # NumPoints
      )
      pm.TagList.Add(tag)

    pm.RetrievalMode  = "Average"
    pm.CalculationBasis  = "Time Weighted"
    pm.SummaryDuration = "10s"
    pm.Timezone = "Local"

    ds  = DataSourceImpl(pm);
    dataTableName = "Data_{}_{}".format(year, quarter)
    if  Document.Data.Tables.Contains(dataTableName):
      Document.Data.Tables[dataTableName].ReplaceData(ds)
    else:
      Document.Data.Tables.Add(dataTableName, ds)
