
<h2 id="Connecting-to-impala-on-a-mac">Connecting to impala with R on a mac<a class="anchor-link" href="#Connecting-to-impala-on-a-mac"></a></h2>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This is a little more complicated than connecting with Python and requires the use of ODBC drivers and the RODBC package. </p>
<p>**Note: The RImpala package connects to impala more easily, but doesn't run useful queries so it won't be covered here.</p>
<p>For Windows instructions, click <a href='https://github.com/summerela/impala_training/blob/master/connect_r_windows.md' target='_blank'>here.</a></p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Install-unixODBC-drivers">1. Install UNIX ODBC drivers<a class="anchor-link" href="#Install-unixODBC-drivers"></a></h3>
</div>
</div>
</div>


<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">brew</span> <span class="n">install</span> <span class="n">unixodbc</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Install-the-Impala-ODBC-Driver">2. Install the Impala ODBC Driver<a class="anchor-link" href="#Install-the-Impala-ODBC-Driver"></a></h3>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Downlad and install the Impala ODBC driver from:</p>
<p>http://www.cloudera.com/content/cloudera/en/downloads/connectors/impala/odbc/impala-odbc-v2-5-23.html</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Install-mac-ODBC-manager">3. Install mac ODBC manager<a class="anchor-link" href="#Install-mac-ODBC-manager"></a></h3>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>If the following method doesn't work for you, please see the command line instructions at the bottom of the page:</p>
<ul>
<li> Download file from http://www.odbcmanager.net/ </li>
<li> Once installed, open ODBC manager from Applications/Utilities </li>
<li> Click on Drivers and then Add </li>
<li> Browse to the impala driver, default location is: <br> /opt/cloudera/impalaodbc/lib/universal/libclouderaimpalaodbc.dylib </li>
</ul>
<p>Next, add a System DSN 
<ul>
<li> Click on Add a DSN Name </li>
<li> Click on Add </li>
<li> Add the following two key-value pairs: <br>
HOST your_host_name <br>
PORT 21050 </li>
<li> Click on OK </li>
</ul>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Connecting-in-R:">4. Connecting in R:<a class="anchor-link" href="#Connecting-in-R:"></a></h3>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>After the ODBC drivers are setup, it's easy to query impala in R using the RODBC package.</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="c">#install the pacakge</span>
<span class="n">install</span><span class="o">.</span><span class="n">packages</span><span class="p">(</span><span class="s">&quot;RODBC&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Once you've installed the RODBC package, you can load the library and create a connection to impala using the DSN name you created on your local machine:</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">library</span><span class="p">(</span><span class="n">RODBC</span><span class="p">)</span>

<span class="c">#connect using the DSN name you created on your machine</span>
<span class="n">conn</span> <span class="o">&lt;-</span> <span class="n">odbcConnect</span><span class="p">(</span><span class="s">&quot;Impala DSN&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Interacting-with-impala">5. Interacting with impala<a class="anchor-link" href="#Interacting-with-impala"></a></h3>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>RODBC uses a collection of sql based functions to perform queries and interact with impala.</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="View-available-databases">View available databases<a class="anchor-link" href="#View-available-databases"></a></h4>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>To view which databases are available in impala, we use the sqlQuery() function on the connection object, and then add a SQL 'SHOW DATABASES' statment:</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">sqlQuery</span><span class="p">(</span><span class="n">conn</span><span class="p">,</span> <span class="s">&#39;SHOW DATABASES&#39;</span><span class="p">)</span>

              <span class="n">name</span>
<span class="mi">1</span> <span class="n">_impala_builtins</span>
<span class="mi">2</span>          <span class="n">default</span>
<span class="mi">3</span>           <span class="n">p7_ptb</span>
<span class="mi">4</span>            <span class="n">p7dev</span>
<span class="mi">5</span>      <span class="n">public_hg19</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="View-available-tables">View available tables<a class="anchor-link" href="#View-available-tables"></a></h4>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>To available all available tables, use the sqlTables() function on your connection object.</p>
<p>The TABLE_SCHEM column shows you which database the table is located in, and the TABLE_NAME column shows you the tables in each database.</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">sqlTables</span><span class="p">(</span><span class="n">conn</span><span class="p">)</span>

    <span class="n">TABLE_CAT</span> <span class="n">TABLE_SCHEM</span>            <span class="n">TABLE_NAME</span> <span class="n">TABLE_TYPE</span> <span class="n">REMARKS</span>
<span class="mi">1</span>     <span class="n">Impala</span>     <span class="n">default</span>            <span class="n">feature_fm</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">2</span>     <span class="n">Impala</span>     <span class="n">default</span>         <span class="n">featurematrix</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">3</span>     <span class="n">Impala</span>     <span class="n">default</span>              <span class="n">features</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">4</span>     <span class="n">Impala</span>     <span class="n">default</span>  <span class="n">fmx_ptb_df4_clinical</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">5</span>     <span class="n">Impala</span>     <span class="n">default</span>             <span class="n">mastervar</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">6</span>     <span class="n">Impala</span>     <span class="n">default</span>      <span class="n">ptb_illumina_all</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">7</span>     <span class="n">Impala</span>     <span class="n">default</span> <span class="n">ptb_illumina_variants</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Viewing-more-information-about-a-table">Viewing more information about a table<a class="anchor-link" href="#Viewing-more-information-about-a-table"></a></h4>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Before pulling information from tables, its helpful to take a look at columns and data types available in each table. We can do this using SQL DESCRIBE statement:</p>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="c">#use the format &#39;database.table&#39; to select a particular table</span>
<span class="n">sqlQuery</span><span class="p">(</span><span class="n">conn</span><span class="p">,</span> <span class="s">&#39;DESCRIBE public_hg19.cytoband&#39;</span><span class="p">)</span>

        <span class="n">name</span>   <span class="nb">type</span>                   <span class="n">comment</span>
<span class="mi">1</span>      <span class="n">chrom</span> <span class="n">string</span>         <span class="n">Chromosome</span> <span class="n">number</span>
<span class="mi">2</span> <span class="n">chromstart</span>    <span class="nb">int</span> <span class="n">Start</span> <span class="n">position</span> <span class="ow">in</span> <span class="n">genoSeq</span>
<span class="mi">3</span>   <span class="n">chromend</span>    <span class="nb">int</span>   <span class="n">End</span> <span class="n">position</span> <span class="ow">in</span> <span class="n">genoSeq</span>
<span class="mi">4</span>       <span class="n">name</span> <span class="n">string</span>  <span class="n">Name</span> <span class="n">of</span> <span class="n">cytogenetic</span> <span class="n">band</span>
<span class="mi">5</span>   <span class="n">giestain</span> <span class="n">string</span>      <span class="n">Giesma</span> <span class="n">stain</span> <span class="n">results</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Installing-ODBC-drivers-from-the-command-line">Installing ODBC drivers from the command line<a class="anchor-link" href="#Installing-ODBC-drivers-from-the-command-line"></a></h3>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>If the above method doesn't work for you, you might need to go command line. I apologize in advance, this isn't going to be pleasant.</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><h4>1. <a href='http://www.cloudera.com/content/cloudera/en/downloads/connectors/impala/odbc/impala-odbc-v2-5-23.html' target='_blank'>Download</a> and install the impala ODBC driver.</h4></p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Install-UNIX-ODBC-drivers-and-view-installed-location:">2. Install UNIX ODBC drivers and view installed location:<a class="anchor-link" href="#Install-UNIX-ODBC-drivers-and-view-installed-location:"></a></h4>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>brew install unixodbc odbcinst -j</p>
<p>unixODBC 2.3.2 DRIVERS............: /usr/local/etc/odbcinst.ini SYSTEM DATA SOURCES: /usr/local/etc/odbc.ini FILE DATA SOURCES..: /usr/local/etc/ODBCDataSources USER DATA SOURCES..: /Users/summerrae/.odbc.ini SQLULEN Size.......: 8 SQLLEN Size........: 8 SQLSETPOSIROW Size.: 8</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Point-the-DYLD-library-path-variable:">3. Point the DYLD library path variable:<a class="anchor-link" href="#Point-the-DYLD-library-path-variable:"></a></h4>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">export</span> <span class="n">DYLD_LIBRARY_PATH</span><span class="o">=</span><span class="err">$</span><span class="n">DYLD_LIBRARY_PATH</span><span class="p">:</span><span class="o">/</span><span class="n">opt</span><span class="o">/</span><span class="n">cloudera</span><span class="o">/</span><span class="n">impalaodbc</span><span class="o">/</span><span class="n">lib</span><span class="o">/</span><span class="n">universal</span>
<span class="n">echo</span> <span class="s">&quot;export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/opt/cloudera/impalaodbc/lib/universal/&quot;</span> <span class="o">&gt;&gt;</span> <span class="o">~/.</span><span class="n">bashrc</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Edit-/usr/local/etc/odbc.ini:">4. Edit /usr/local/etc/odbc.ini:<a class="anchor-link" href="#Edit-/usr/local/etc/odbc.ini:"></a></h4>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="p">[</span><span class="n">ODBC</span> <span class="n">Data</span> <span class="n">Sources</span><span class="p">]</span>
<span class="c"># Use this name in your connection string </span>
<span class="n">Impala</span> <span class="n">DSN</span><span class="o">=</span><span class="n">Impala</span> <span class="n">ODBC</span> <span class="n">Driver</span>
<span class="p">[</span><span class="n">Impala</span> <span class="n">DSN</span><span class="p">]</span>
<span class="c"># Driver: The location where the ODBC driver is installed to. </span>
<span class="n">Driver</span><span class="o">=/</span><span class="n">opt</span><span class="o">/</span><span class="n">cloudera</span><span class="o">/</span><span class="n">impalaodbc</span><span class="o">/</span><span class="n">lib</span><span class="o">/</span><span class="n">universal</span><span class="o">/</span><span class="n">libclouderaimpalaodbc</span><span class="o">.</span><span class="n">dylib</span>
<span class="c"># Values for HOST, PORT, Database </span>
<span class="n">HOST</span><span class="o">=</span><span class="n">myhost</span> <span class="p">(</span><span class="n">changed</span> <span class="n">name</span> <span class="n">here</span> <span class="k">for</span> <span class="n">security</span><span class="p">)</span>
<span class="n">PORT</span><span class="o">=</span><span class="mi">21050</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Edit-/user/local/etc/odbcinst.ini">5. Edit /user/local/etc/odbcinst.ini<a class="anchor-link" href="#Edit-/user/local/etc/odbcinst.ini"></a></h4>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="p">[</span><span class="n">ODBC</span> <span class="n">Drivers</span><span class="p">]</span>
<span class="n">Impala</span> <span class="n">ODBC</span> <span class="n">Driver</span><span class="o">=</span><span class="n">Installed</span>
<span class="p">[</span><span class="n">Impala</span> <span class="n">ODBC</span> <span class="n">Driver</span><span class="p">]</span>
<span class="n">Description</span><span class="o">=</span><span class="n">Impala</span> <span class="n">ODBC</span> <span class="n">Driver</span>
<span class="n">Driver</span><span class="o">=/</span><span class="n">opt</span><span class="o">/</span><span class="n">cloudera</span><span class="o">/</span><span class="n">impalaodbc</span><span class="o">/</span><span class="n">lib</span><span class="o">/</span><span class="n">universal</span><span class="o">/</span><span class="n">libclouderaimpalaodbc</span><span class="o">.</span><span class="n">dylib</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Edited-/opt/cloudera/impalaodbc/lib/universal/cloudera.impalaodbc.ini:">6. Edit /opt/cloudera/impalaodbc/lib/universal/cloudera.impalaodbc.ini:<a class="anchor-link" href="#Edited-/opt/cloudera/impalaodbc/lib/universal/cloudera.impalaodbc.ini:"></a></h4>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="p">[</span><span class="n">Driver</span><span class="p">]</span>
<span class="c">## - Note that this default DriverManagerEncoding of UTF-15 </span>
<span class="c">## is for unixODBC. </span>
<span class="n">DriverManagerEncoding</span><span class="o">=</span><span class="n">UTF</span><span class="o">-</span><span class="mi">16</span>
<span class="n">ErrorMessagesPath</span><span class="o">=/</span><span class="n">opt</span><span class="o">/</span><span class="n">cloudera</span><span class="o">/</span><span class="n">impalaodbc</span><span class="o">/</span><span class="n">ErrorMessages</span><span class="o">/</span>
<span class="n">LogLevel</span><span class="o">=</span><span class="mi">0</span>
<span class="n">LogPath</span><span class="o">=</span>

<span class="c">## - Note that the path to your ODBC Driver Manager </span>
<span class="c">## must be specified in DYLD_LIBRARY_PATH.</span>
<span class="c"># unixODBC </span>
<span class="n">ODBCInstLib</span><span class="o">=</span><span class="n">libiodbcinst</span><span class="o">.</span><span class="n">dylib</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Export-path-variables-to-~/.bashrc:">7. Export path variables to ~/.bashrc:<a class="anchor-link" href="#Export-path-variables-to-~/.bashrc:"></a></h4>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="c">#add full path to odbc.ini and add to bashrc</span>
<span class="n">export</span> <span class="n">ODBCINI</span><span class="o">=/</span><span class="n">usr</span><span class="o">/</span><span class="n">local</span><span class="o">/</span><span class="n">etc</span><span class="o">/</span><span class="n">odbc</span><span class="o">.</span><span class="n">ini</span>
<span class="n">echo</span> <span class="s">&quot;export ODBCINI=/etc/odbc.ini&quot;</span> <span class="o">&gt;&gt;</span> <span class="o">~/.</span><span class="n">bashrc</span>

<span class="c">#add directory path to odbcinst.ini and add to bashrc</span>
<span class="n">export</span> <span class="n">ODBCSYSINI</span><span class="o">=/</span><span class="n">usr</span><span class="o">/</span><span class="n">local</span><span class="o">/</span><span class="n">etc</span><span class="o">/</span>
<span class="n">echo</span> <span class="s">&quot;export ODBCSYSINI=/etc/odbcinst.ini&quot;</span> <span class="o">&gt;&gt;</span> <span class="o">~/.</span><span class="n">bashrc</span>

<span class="c">#add full path to cloudera.impalaodbc.ini and add to bashrc</span>
<span class="n">export</span> <span class="n">CLOUDERAIMPALAINI</span><span class="o">=/</span><span class="n">opt</span><span class="o">/</span><span class="n">cloudera</span><span class="o">/</span><span class="n">impalaodbc</span><span class="o">/</span><span class="n">lib</span><span class="o">/</span><span class="n">universal</span><span class="o">/</span><span class="n">cloudera</span><span class="o">.</span><span class="n">impalaodbc</span><span class="o">.</span><span class="n">ini</span>
<span class="n">echo</span> <span class="s">&quot;export CLOUDERAIMPALAINI=/opt/cloudera/impalaodbc/lib/universal/cloudera.impalaodbc.ini&quot;</span> <span class="o">&gt;&gt;</span> <span class="o">~/.</span><span class="n">bashrc</span>
</pre></div>

</div>
</div>
</div>

</div>
    </div>
  </div>
</body>
</html>
