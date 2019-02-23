/*
 * File name: main.js
 * Author: Yuchang Zhang
 * Date: 02/04/2018
 * Description:
 * 		This is the main renderer process of the JS/html based electron app. There can be only one main process which is named main.js.
 * 		This file include one BrowserWindow instance, this also initiate functionalities of the top window.
 */

// Modules to control application life and create native browser window
const {app, BrowserWindow, Menu} = require('electron')

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow
let child

function createWindow () {
  // Create the browser window.
  mainWindow = new BrowserWindow({width: 1080, height: 360})

  // and load the home.html of the app.
  mainWindow.loadFile('home.html')

  
  // Build menu from template
  const mainMenu = Menu.buildFromTemplate(mainMenuTemplate)
	
	// Insert menu
  Menu.setApplicationMenu(mainMenu)
	
	
	
  child = new BrowserWindow({parent: mainWindow, modal: true, show: false})
	
  child.loadURL(`file://${__dirname}/setting.html`)
  // Open the DevTools.
//  mainWindow.webContents.openDevTools()
  child.webContents.openDevTools()

  // Emitted when the window is closed.
  mainWindow.on('closed', function () {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows, this is the time
    // when you should delete the corresponding element.
    mainWindow = null
  })
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', function () {
  // On OS X it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', function () {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) {
    createWindow()
  }
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.

// Menu Template here
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
