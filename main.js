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
	mainWindow.loadURL(url.format({
		path: path.join('$PWD', 'mainWindow.html'),
		protocol: '~',		//'file:',
		slashes: true
	}));
	
	// Build menu from template
	const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
	// Insert menu
	Menu.setApplicationMenu(mainMenu);
});


// Create Menu template
const mainMenuTemplate = [
	{
		label:'file',
		submenu:[
			{
				label: 'sub1'
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
		label:'edit',
		submenu:[
			{
				label: 'sub1'
			},
			{
				label: 'sub2'
			}
		]
	}
]