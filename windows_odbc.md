<h2 id="Connecting-to-impala-on-windows">Connecting to impala on windows<a class="anchor-link" href="#Connecting-to-impala-on-windows"></a></h2>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Connecting to impala requires the use of the impala ODBC driver. Install it by going through the following steps in order: </p>
<p> For mac instructions, click <a href='https://github.com/summerela/impala_training/blob/master/mac_odbc.md' target='_blank'>here.</a>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Install-the-Impala-ODBC-Driver">1. Install the Impala ODBC Driver<a class="anchor-link" href="#Install-the-Impala-ODBC-Driver"></a></h3>
</div>
</div>
</div>

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Download and install the Impala ODBC driver from:</p>
<p>http://www.cloudera.com/content/cloudera/en/downloads/connectors/impala/odbc/impala-odbc-v2-5-23.html</p>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Install-Cloudera-Impala-ODBC-driver">2. Install Cloudera Impala ODBC driver<a class="anchor-link" href="#Install-Cloudera-Impala-ODBC-driver"></a></h3>
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
