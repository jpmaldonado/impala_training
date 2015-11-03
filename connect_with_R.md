<h3>Connecting to impala with R</h3>
Once you've <a href='https://github.com/summerela/impala_training/blob/master/connect_r_mac.md' target='_blank'>created an ODBC DSN</a> on your machine, you can connect to R using the RODBC package:
    
    #run first-time only
    install.packages("RODBC")
     
     library(RODBC)
     
     #connect using the DSN name you created on your machine
     conn <- odbcConnect("Cloudera Impala DSN")

<h3>View available databases and tables</h3>
To view what tables are available on impala, run the sqlTables() function on the connection object:

    sqlTables(conn)
    
    TABLE_CAT    TABLE_SCHEM       TABLE_NAME   TABLE_TYPE     REMARKS
    IMPALA        default          clarity      TABLE          <NA>
    IMPALA        default          clin_path    TABLE          <NA>
    IMPALA        default          feature_fm   TABLE          <NA>
    
  <h3>View the explain plan</h3>
  
  To view the explain plan for any query, simply type 'EXPLAIN' before the query: 
  
    # view explain plan
    query = "EXPLAIN SELECT * FROM p7_ref_grch37.ucsc_knowngene WHERE chrom = '1' LIMIT 5"
    sqlQuery(conn, query)
    
  <h3>Read a table into a data frame</h3>
  We can pull a specific table into a data frame using sqlFetch() and the format database_name.table_name:
  
    #select tables using the format database.table
    ucsc.df <- sqlFetch(conn, "p7_ref_grch37.ucsc_genes")
    
To make this more efficient, we can also limit the number of rows we pull in using "max":
  
    #select tables using the format "database_name.table_name"
    sqlFetch(conn, "p7_ref_grch37.ucsc_genes", max=5)
    
    ucsc_id      chrom strand   txstart txend   cdsstart cdsend     exoncount
    uc001aaa.3     1      +      11874  14409    11873    11873         3
    uc010nxr.1     1      +      11874  14409    11873    11873         3
    uc010nxq.1     1      +      11874  14409    12189    13639         3
    uc009vis.3     1      -      14362  16765    14361    14361         4
    uc009vit.3     1      -      14362  19759    14361    14361         9
