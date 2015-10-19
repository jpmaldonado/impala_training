#Run only the first time to install the package
install.packages("RODBC",type = "source")

#load RODBC library
library(RODBC)

# Connect to impala  

#create a connection object using your DSN
conn <- odbcConnect("Impala_DSN")
print(conn)

# interact with impala using your connection object
 
## View databases and tables 
sqlTables(conn)

#select tables using the format database.table and sqlFetch()
ucsc.df <- sqlFetch(conn, "p7_ref_grch37.ucsc_knowngene")
head(ucsc.df)

# Run queries using your connection object and the sqlQuery() function
query = "SELECT * FROM p7_ref_grch37.ucsc_knowngene WHERE chrom = '1' LIMIT 5"
sqlQuery(conn, query)

# save query results as a dataframe
query = "SELECT * FROM p7_ref_grch37.ucsc_knowngene WHERE chrom = '1' LIMIT 5"
results = sqlQuery(conn, query)
print (results)

#don't forget to close the connection
#or you could leave a long query running...and running...and...
odbcClose(conn)
