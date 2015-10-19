<h2>Interacting with impala using python</h2>
After you have <a href='https://github.com/summerela/impala_training/blob/master/mac_odbc.md' target='_blank'>setup ODBC drivers</a> on your computer, connecting to impala is easy using the <a href='https://github.com/cloudera/impyla' target='_blank'>impyla</a> or <a href='https://github.com/cloudera/ibis' target='_blank'>ibis</a> module. Since the Ibis module is still under devlopment, this tutorial will only cover the impyla module. 

To install impyla: 

    pip install impyla
    
If pip is not installed on your system, see <a href='http://pip.readthedocs.org/en/stable/installing/' target='_blank'>here</a> or install via anaconda:

    conda install pip
    
<h3>Connecting to impala</h3>
To connect to impala, first create a connection string specifying your impala hostname and port. The default port for impala is 21050. 

Once you setup the connection string, you can create a cursor object for intereacting with the database: 

    from impala.dbapi import connect

    #create a connection 
    conn=connect(host='impala_host', port=21050)

    #to connect to specific database, use the database argument
    #conn=connect(host='impala_host', port=21050, database="public_hg19")

    #create a cursor object to interact with the db
    cur = conn.cursor()
    

