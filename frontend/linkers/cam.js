function streaming(){
	var python = require("python-shell")
	var path = require("path")
	
	var option = {
	scriptPath : '/Users/yuchangzhang/git/OSIMS/backend/streaming',
		//`/Users/yuchangzhang/git/OSIMS/backend/streaming`,
		//path.join(__dirname, '/../../backend/streaming/'),
	pythonPath : '/usr/local/bin/python3.7'
	}
	
	var video = new python("cam.py", options);
	
}