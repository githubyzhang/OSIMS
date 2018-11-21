const electron = require('electron');
const url = require('url');
var path = require('path');

const {app, BrowserWindow, Menu} = electron;

let mainWindow;

// listen for app to be ready
app.on('ready', function(){
	// Create new window
	mainWindow = new BrowserWindow({
		width: 1281,
		height: 800,
		minWidth: 1281,
		//backgroundColor: '#312450',
		minHeight: 800,
		icon: path.join(__dirname, '/front_end/OSIMS_icon.png')
	});
	
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
						label: 'Hot Corner',
						accelerator: process.platform == 'darwin' ? 'Command+H' : 'Ctrl+H'
					},
					{
						label: 'Temperature Cursor',
						accelerator: process.platform == 'darwin' ? 'Command+T' : 'Ctrl+T'
					},
				]
			},
			{
				label: 'Tools Manager'
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