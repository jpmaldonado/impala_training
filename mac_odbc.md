
<h2 id="Connecting-to-impala-on-a-mac">Connecting to impala on a mac<a class="anchor-link" href="#Connecting-to-impala-on-a-mac"></a></h2>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
You will need to download the impala ODBC driver that is compatible with your version of impala (if unsure, just download the latest version) and follow the steps outlined below in order.</p>
<p>For Windows instructions, click <a href='https://github.com/summerela/impala_training/blob/master/windows_odbc.md' target='_blank'>here.</a></p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
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



