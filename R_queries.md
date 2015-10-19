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
    
    TABLE_CAT    TABLE_SCHEM                       TABLE_NAME TABLE_TYPE REMARKS
    IMPALA        default                          clarity      TABLE    <NA>
    IMPALA        default                        clin_path      TABLE    <NA>
    IMPALA        default                       feature_fm      TABLE    <NA>
    
  <h3>Read a table into a data frame</h3>
  We can pull a specific table into a data frame using sqlFetch() and the format database_name.table_name:
  
    #select tables using the format database.table
    ucsc.df <- sqlFetch(conn, "p7_ref_grch37.ucsc_genes")
    
To make this more efficient, we can also limit the number of rows we pull in using "max":
  
    #select tables using the format "database_name.table_name"
    sqlFetch(conn, "p7_ref_grch37.ucsc_genes", max=5)
    
    ucsc_id chrom strand txstart txend cdsstart cdsend exoncount
    uc001aaa.3     1      +   11874 14409    11873  11873         3
    uc010nxr.1     1      +   11874 14409    11873  11873         3
    uc010nxq.1     1      +   11874 14409    12189  13639         3
    uc009vis.3     1      -   14362 16765    14361  14361         4
    uc009vit.3     1      -   14362 19759    14361  14361         9
    
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
    
    ucsc_id chrom strand txstart txend cdsstart cdsend exoncount
    uc001aaa.3     1      +   11874 14409    11873  11873         3
    uc010nxr.1     1      +   11874 14409    11873  11873         3
    uc010nxq.1     1      +   11874 14409    12189  13639         3
    uc009vis.3     1      -   14362 16765    14361  14361         4
    uc009vit.3     1      -   14362 19759    14361  14361         9
    
That still returns a lot of data. We can get more specific and select only genes on chromosome 1 that are on the forward strand: 

    sqlQuery(conn, "SELECT * 
    FROM p7_ref_grch37.ucsc_genes 
    WHERE chrom = '1' 
    AND strand = '+'
    LIMIT 5")

    ucsc_id chrom strand txstart  txend cdsstart cdsend exoncount         
    uc001aaa.3     1      +   11874  14409    11873  11873         3 
    uc010nxr.1     1      +   11874  14409    11873  11873         3 
    uc010nxq.1     1      +   11874  14409    12189  13639         3 
    uc001aal.1     1      +   69091  70008    69090  70008         1  
    uc001aaq.2     1      +  321084 321115   321083 321083         1  
    
<h2>When you need information from more than one table: JOINS</h2>
Pulling together data from multiple tables, such as is done when annotating variants, requires the use of SQL JOIN statements. There are many ways this can be done, let's walk through an example to examine the logic.

For this example we are going to use a table called distinct_test that provides us with basic annotations for each variant found in the Kaviar table. This table provides a DANN score, but for those wanting a more traditional approach, we will also need a corresponding CADD score.  

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

    sqlQuery(conn, "DESCRIBE p7_ref_grch37.cadd")
    
    name     type           comment
    chrom    string         Position on chromosome
    pos      int            1-based position
    raw_a    decimal(7,6)   Raw CADD score for A allele
    raw_c    decimal(7,6)   Raw CADD score for C allele
    raw_g    decimal(7,6)   Raw CADD score for G allele
    raw_t    decimal(7,6)   Raw CADD score for T allele
    phred_a  decimal(4,3)   Phred CADD score for A allele
    phred_c  decimal(4,3)   Phred CADD score for C allele
    phred_g  decimal(4,3)   Phred CADD score for G allele
    phred_t  decimal(4,3)   Phred CADD score for T allele

    
  
