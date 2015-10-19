
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
<p>If this method doesn't work for you, please see the command line instructions in the next section:</p>
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


