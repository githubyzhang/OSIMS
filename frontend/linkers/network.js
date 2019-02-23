/*
 * Author: Yuchang Zhang
 * Date: Feb 4, 2019
 * Function: brd()
 * Description: This function is used to link python backend function cam() to the frontend electron
 * Example: in html file, use <script source=...></script> within <header> to declare the script source
 * 			then uses the script as in <script>streaming()</script>
 */

function addDevice(){
	var ps = require("python-shell")
	var path = require("path")
	var type = document.getElementById("type").value
	var name = document.getElementById("name").value
	var ip = document.getElementById("ip").value
	
	var options = {
	scriptPath : '/Users/yuchangzhang/git/OSIMS/backend/network',
	pythonPath : '/usr/local/bin/python3.7',
	args: [type,name,ip]
	}
	
	ps.PythonShell.run('addDevice.py', options, function (err, results) {
	    if (err) throw err;
	    console.log(results);
	  });
	
}