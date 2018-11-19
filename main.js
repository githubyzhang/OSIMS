const electron = require('electron');
const url = require('url');
const path = require('path');

const {app, BrowserWindow, Menu} = electron;

let mainWindow;

// listen for app to be ready
app.on('ready', function(){
	// Create new window
	mainWindow = new BrowserWindow({});
	
	// Load html into window
	// for somereason doesn't work at the moment, need to figure this out later.
//	mainWindow.loadURL(url.format({
//		path: path.join('/Users/yuchangzhang/git/OSIMS', 'mainWindow.html'),
//		protocol: '~',		//'file:',
//		slashes: true
//	}));
	
	mainWindow.loadFile('mainWindow.html')
	
	// Build menu from template
	const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
	// Insert menu
	Menu.setApplicationMenu(mainMenu);
});


// Create Menu template
const mainMenuTemplate = [
	{
		label:'OSIMS',
		submenu:[
			{
				label: 'About OSIMS'
			},
			{
				label: 'Setting'
			},
			{
				label: 'Quit',
				accelerator: process.platform == 'darwin' ? 'Command+Q' : 'Ctrl+Q',
				click(){
					app.quit();
				}
			}
		]
	},
	
	{
		label:'System',
		submenu:[
			{
				label: 'Configuration'
			},
			{
				label: 'Zone Control',
				submenu:[
					{
						label: 'Zone1'
					},
					{
						label: 'Zone2'
					},
					{
						label: 'Zone2'
					},
				]
			}
		]
	},
	
	{
		label:'Tools',
		submenu:[
			{
				label: 'Select',
				submenu:[
					{
						label: 'Hot Corner'
					},
					{
						label: 'Check Temperature'
					},
				]
			},
			{
				label: 'Tools Manager'
			},
			{
				label: 'Data'
			}
			
		]
	},
	
	{
		label:'Data',
		submenu:[
			{
				label: 'Display Past Data'
			}
		]
	},
	
	{
		label:'Window',
		submenu:[
			{
				label: 'System Control'
			},
			{
				label: 'Tools Manager'
			},
			{
				label: 'Data Panel'
			}
			
		]
	}
]