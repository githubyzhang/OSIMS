/*
 * Author: Yuchang Zhang
 * Date: Feb 1, 2019
 * Function: hcplot()
 * Description: 
 */


function hcplot(){
	var ps = require("python-shell")
	var path = require("path")
	
	var options = {
	scriptPath : '/Users/yuchangzhang/git/OSIMS/backend/streaming',
	pythonPath : '/usr/local/bin/python3.7'
	}
	
	ps.PythonShell.run('hcplot.py', options, function (err, results) {
	    if (err) throw err;
	    console.log(results);
	  });
	
}

function pixelplot(){
	var ps = require("python-shell")
	var path = require("path")
	var xpos = document.getElementById("xpos").value
	var ypos = document.getElementById("ypos").value
	
	var options = {
	scriptPath : '/Users/yuchangzhang/git/OSIMS/backend/streaming',
	pythonPath : '/usr/local/bin/python3.7',
	args: [xpos,ypos]
	}
	
	ps.PythonShell.run('pixelplot.py', options, function (err, results) {
	    if (err) throw err;
	    console.log(results);
	  });
	
}

function warning(){
	var ps = require("python-shell")
	var path = require("path")
	var limit = document.getElementById("limit").value
	
	var options = {
	scriptPath : '/Users/yuchangzhang/git/OSIMS/backend/streaming',
	pythonPath : '/usr/local/bin/python3.7',
	args: [limit]
	}
	
	ps.PythonShell.run('warning.py', options, function (err, results) {
	    if (err) throw err;
	    console.log(results);
	  });
	
}