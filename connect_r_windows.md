<h2 id="Connecting-to-impala-on-windows">Connecting to impala on windows<a class="anchor-link" href="#Connecting-to-impala-on-windows">&#182;</a></h2>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This is a little more complicated than connecting with Python and requires the use of ODBC drivers.</p>
<p>**Note: The RImpala package connects to impala, but the queries don't work, so its useless.</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Install-the-Impala-ODBC-Driver">Install the Impala ODBC Driver<a class="anchor-link" href="#Install-the-Impala-ODBC-Driver">&#182;</a></h3>
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
<h3 id="Install-Cloudera-Impala-ODBC-driver">Install Cloudera Impala ODBC driver<a class="anchor-link" href="#Install-Cloudera-Impala-ODBC-driver">&#182;</a></h3>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The installation of the Impala ODBC drivers adds an ODBC manager program that allows for easy installation of the drivers:</p>
<ul>
<li>Click on Start/All Programs/Cloudera ODBC Driver../(32 or 64)bit Administrator</li>
<li>Click on the &quot;Drivers&quot; tab to make sure driver is installed</li>
<li>Click on the &quot;System DSN&quot; tab</li>
<li>Select the Sample Cloudera Imapala ODBC driver and click &quot;Configure&quot;</li>
<li>Change the following entries:
<ul>
<li>Data Source Cloudera Impala DSN</li>
<li>Description: Cloudera Impala DSN</li>
<li>Host: glados19</li>
</ul></li>
<li>Click on &quot;Test&quot; to make sure your connection works</li>
</ul>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Connecting-in-R:">Connecting in R:<a class="anchor-link" href="#Connecting-in-R:">&#182;</a></h3>
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
<h3 id="Interacting-with-impala">Interacting with impala<a class="anchor-link" href="#Interacting-with-impala">&#182;</a></h3>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>RODBC uses a collection of sql based functions to perform queries and interact with impala. For more advanced queries, please visit:</p>
<p>{link to page when it's on confluence}</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="View-available-databases">View available databases<a class="anchor-link" href="#View-available-databases">&#182;</a></h4>
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
<h4 id="View-available-tables">View available tables<a class="anchor-link" href="#View-available-tables">&#182;</a></h4>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>To available all available talbes, use the sqlTables() function on your connection object.</p>
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
<span class="mi">8</span>     <span class="n">Impala</span>     <span class="n">default</span>           <span class="n">ptb_samples</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">9</span>     <span class="n">Impala</span>     <span class="n">default</span>               <span class="n">samples</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">10</span>    <span class="n">Impala</span>      <span class="n">p7_ptb</span>        <span class="n">comgen_variant</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">11</span>    <span class="n">Impala</span>      <span class="n">p7_ptb</span>      <span class="n">illumina_variant</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">12</span>    <span class="n">Impala</span>      <span class="n">p7_ptb</span>       <span class="n">variant_summary</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">13</span>    <span class="n">Impala</span>       <span class="n">p7dev</span>        <span class="n">refseq_map_tsv</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">14</span>    <span class="n">Impala</span>       <span class="n">p7dev</span>     <span class="n">refseq_map_tsv_gz</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">15</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>               <span class="n">clinvar</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">16</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>       <span class="n">clinvar_summary</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">17</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>              <span class="n">cytoband</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">18</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>                 <span class="n">dbsnp</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">19</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>         <span class="n">ensembl_genes</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">20</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>            <span class="n">esp_exomes</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">21</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>                <span class="n">kaviar</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">22</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>               <span class="n">mirbase</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">23</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>            <span class="n">pfam_clans</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">24</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>          <span class="n">pfam_regions</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">25</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>                <span class="n">refseq</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">26</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>            <span class="n">refseq_map</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">27</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>          <span class="n">repeatmasker</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">28</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>                  <span class="n">ucsc</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
<span class="mi">29</span>    <span class="n">Impala</span> <span class="n">public_hg19</span>           <span class="n">ucsc_segdup</span>      <span class="n">TABLE</span>    <span class="o">&lt;</span><span class="n">NA</span><span class="o">&gt;</span>
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
<h4 id="Viewing-more-information-about-a-table">Viewing more information about a table<a class="anchor-link" href="#Viewing-more-information-about-a-table">&#182;</a></h4>
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
<p>To learn more about creating queries, please visit: https://ilyawiki.systemsbiology.net/display/ISBInova/Creating+impala+queries</p>
</div>
</div>
</div>
    </div>
  </div>
</body>
</html>
