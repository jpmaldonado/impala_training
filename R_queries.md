<h2> Querying Impala with R </h2>

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
    
<h2>Building Queries</h2>
Pulling down entire tables is not very efficient, so let's use impala queries to filter for just the data we need. Impala queries are basically SQL queries that follow variations of this basic format:

    SELECT column_name(s) FROM database.table
    WHERE conditions
    GROUP BY (use only if you want to aggregate data in some way)
    LIMIT number of rows to return (omit this statement to return all matches)
    
For example, to select only genes on chromosome 1 from the ucsc table, use the sqlQuery() function and the format outlined above:

    sqlQuery(conn, "SELECT * 
    FROM p7_ref_grch37.ucsc_genes 
    WHERE chrom = '1' 
    LIMIT 5")
    
    ucsc_id      chrom strand txstart txend  cdsstart cdsend   exoncount
    uc001aaa.3     1      +   11874   14409    11873  11873         3
    uc010nxr.1     1      +   11874   14409    11873  11873         3
    uc010nxq.1     1      +   11874   14409    12189  13639         3
    uc009vis.3     1      -   14362   16765    14361  14361         4
    uc009vit.3     1      -   14362   19759    14361  14361         9
    
That still returns a lot of data. We can get more specific and select only genes on chromosome 1 that are on the forward strand: 

    sqlQuery(conn, "SELECT * 
    FROM p7_ref_grch37.ucsc_genes 
    WHERE chrom = '1' 
    AND strand = '+'
    LIMIT 5")

    ucsc_id     chrom strand txstart  txend   cdsstart cdsend    exoncount         
    uc001aaa.3     1      +   11874   14409    11873   11873         3 
    uc010nxr.1     1      +   11874   14409    11873   11873         3 
    uc010nxq.1     1      +   11874   14409    12189   13639         3 
    uc001aal.1     1      +   69091   70008    69090   70008         1  
    uc001aaq.2     1      +  321084   321115   321083  321083        1  
    
<h2>When you need information from more than one table: JOINS</h2>
Pulling together data from multiple tables, such as is done when annotating variants, requires the use of SQL JOIN statements. There are many ways this can be done, let's walk through an example to examine the logic.

For this example we are going to use a table called distinct_test that provides us with basic annotations for each variant found in the Kaviar table. This table provides basic annotaitons, but does not contain information on cytobands, so we'll need to join it with the cytoband table.  

Since we don't know the structure of these tables yet, before we can pull data from them we need to figure out what fields we can use to match the tables on. 

We can get more information about the columns in each table by using a DESCRIBE statement:

    # before joining, view table structure using "DESCRIBE database.table_name"
    sqlQuery(conn, "DESCRIBE users_selasady.distinct_test")    
    
    name           type                comment
    chrom          string              Chromosome
    pos            int                 Variant position on chromosome
    ref            string              Reference allele
    alt            string              Alternate allele
    kav_freq       float               Kaviar allele frequency.
    clin_sig       string              ClinVar clinical significance rating
    clin_dbn       string              ClinVar definition
    rs_id          string              rsID from dbSNP
    dann_score     decimal(18,17)      DANN pathogenicity score
    ens_gene       string              Ensembl gene name
    ens_geneid     string              Ensembl gene ID
    
The DESCRIBE statement tells you what columns are available in your table, the data type of each column, and possibly a brief description about what is contained in each column as a comment. 

    sqlQuery(conn, "DESCRIBE p7_ref_grch37.cytoband")
    
    name       type        comment
    chrom      string      Chromosome number
    start      int         Start position in genoSeq (renamed from chromstart)
    stop       int         End position in genoSeq (renamed from chromend)
    name       string      Name of cytogenetic band
    gie_stain string       Giesma stain results (renamed from gieStain)

After examining the structure of each table, we can locate common columns to join the tables on: 

    distinct_test    cytoband
    ______________________
    chrom            chrom
    pos              start
                     stop
                     
We can join these tables by finding variants whose chromsome matches a cytoband chromsome, and whose position falls between a cytobands start and stop positions. 

<h4>SELECT</h4>
Now we need to figure out what information we want to get back from each table. Since we are already have basic annotations in the distinct_test table, we'll want to keep everything from that table. All we need from the cytoband table are the 'name' and 'gie_stain' information. 

Here's our opening statement:

    SELECT dist.*, cyto.name, cyto.gie_stain
    
Wait. What's this dist. and cyto. stuff? In the following step, we're going to nickname each source database so that it's easier to keep track of what columns came from which tables without having to type out the full table name every time. It's called <b>aliasing</b>.   
  
    users_selasady.distinct_test = dist
    ref_grch37.cytoband = cyto
    
<h4>FROM</h4>
Here's where we tell impala what table(s) to get the information from. And where we give each table an alias so we can be lazy typers.

    FROM users_selasady.distinct_test as dist, ref_grch37.cytoband as cyto
    
<h4>WHERE</h4>
Now we need to give impala some parameters on how to match the data. And this is where the aliased names really come in handy. We are going to match the tables where chromosomes are equal and the variaint position falls between the cytoband start and stop sites. 

The first statment starts with WHERE, and each following clause starts with AND. 

Since the chromosome field can contain letters and not just numbers, its data type is a string and therefore must be placed in quotes, as shown below:

    WHERE dist.chrom = cyto.chrom
    AND dist.pos BETWEEN cyto.start and cyto.stop

The WHERE clause is used to filter data sets, so it's perfect for subsetting data. You can also use the following operators:

| Operator | Description | 
| _________| ____________|
|     =	   |    Equal    |
!=	Not equal
>	Greater than
< 	Less than
>= 	Greater than or equal
<=	Less than or equal
BETWEEN	Between inclusive range
LIKE	Search for pattern
IN	Specify multiple possible values
EXISTS	Return values that match parameters in suqbuery
NOT EXISTS	Return all values that don't match parameters in subquery
