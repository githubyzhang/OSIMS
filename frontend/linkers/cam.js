/*
 * Author: Yuchang Zhang
 * Date: Feb 1, 2019
 * Function: streaming()
 * Description: This function is used to link python backend function cam() to the frontend electron
 * Example: in html file, use <script source=...></script> within <header> to declare the script source
 * 			then uses the script as in <script>streaming()</script>
 */


function streaming(){
	var ps = require("python-shell")
	var path = require("path")
	var mode = document.getElementById("mode").value
	var maxval = document.getElementById("maxval").value
	var minval = document.getElementById("minval").value
	
	var options = {
	scriptPath : '/Users/yuchangzhang/git/OSIMS/backend/streaming',
	pythonPath : '/usr/local/bin/python3.7',
	args: [mode,minval,maxval]
	}
	
	ps.PythonShell.run('stream.py', options, function (err, results) {
	    if (err) throw err;
	    console.log(results);
	  });
	
}