/*
 * File name: main.js
 * Author: Yuchang Zhang
 * Date: 11/24/2018
 * Description:
 * 		This is the main renderer process of the JS/html based electron app. There can be only one main process which is named main.js.
 * 		This file include one BrowserWindow instance, this also initiate functionalities of the top window.
 */


const electron = require('electron');
const url = require('url');
var path = require('path');
const {app, BrowserWindow, Menu} = electron;

let mainWindow;
let child;


// listen for app to be ready
app.on('ready', function(){
	// Create new window
	mainWindow = new BrowserWindow({
		width: 1400,
		height: 1000,
		minWidth: 1282,
		//backgroundColor: '#312450',
		minHeight: 800,
		icon: path.join(__dirname, '/front_end/OSIMS_icon.png')
	});
	
	
	// Load html into window
	mainWindow.loadURL(`file://${__dirname}/html/mainWindow.html`);
							//	mainWindow.loadFile('mainWindow.html');
	
	// Build menu from template
	const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
	
	// Insert menu
	Menu.setApplicationMenu(mainMenu);
	
	
	
	child = new BrowserWindow({parent: mainWindow, modal: true, show: false});
	
	child.loadURL(`file://${__dirname}/html/settingWindow.html`);
	
	
});







/*
 * Function: mainMenuTemplate()
 * Author: Yuchang Zhang
 * Description: This build the mainMenu and use for the main window of OSIMS app.
 */ 
const mainMenuTemplate = [
	{
		label:'OSIMS',
		submenu:[
			{
				label: 'About OSIMS'
			},
			{
				label: 'Setting',
				click(){
				  child.show();
				}
				
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
						label: 'Zone3'
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