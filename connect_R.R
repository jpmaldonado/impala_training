###################
## Setup Package ##
###################

#Run first time to install the package
install.packages("RODBC",type = "source")

#load RODBC library
library(RODBC)

########################
## Connect to impala  ##
########################

#create a connection object using the DSN created during your ODBC setup
conn <- odbcConnect("Impala_DSN")
print(conn)

##################
## Query Impala ##
##################

## View databases and tables 
sqlTables(conn)

#import tables as dataframes using sqlFetch(conn, 'database.table_name')
cytoband.df <- sqlFetch(conn, "p7_ref_grch37.cytoband")
head(cytoband.df)

# Run queries using your connection object and sqlQuery(conn, 'query')
query = "SELECT * FROM p7_ref_grch37.cytoband WHERE chrom = '1' LIMIT 5"
sqlQuery(conn, query)

# Viewing explain plan
# Run queries using your connection object and sqlQuery(conn, 'query')
query = "EXPLAIN SELECT * FROM p7_ref_grch37.ucsc_knowngene WHERE chrom = '1' LIMIT 5"
sqlQuery(conn, query)

# save query results as a dataframe
query = "SELECT * FROM p7_ref_grch37.cytoband WHERE chrom = '1' LIMIT 5"
results = sqlQuery(conn, query)
print (results)

# save dataframe to impala
sqlSave(conn, results, tablename='training.r_test', rownames=FALSE)

#don't forget to close the connection
#or you could leave a long query running...and running...and...
odbcClose(conn)
