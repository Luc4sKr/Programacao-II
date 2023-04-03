const { app, BrowserWindow, ipcMain } = require('electron');
const path = require("path");

const ipc = ipcMain;

const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        minWidth: 940,
        minHeight: 560,

        frame: false,

        webPreferences: {
            preload: path.join(__dirname, "preload.js"),

            nodeIntegration: true,
            contextIsolation: false,
            devTools: true
        }
    });

    win.loadFile('src/index.html')
    win.setBackgroundColor("#001d3d");

    ///// close app
    ipc.on("closeApp", () => {
        win.close();
    });

    ///// minimize app
    ipc.on("minimizeApp", () => {
        win.minimize();
    });

    ///// maximize app
    ipc.on("maximizeRestoreApp", () => {
        if (win.isMaximized()) {
            win.restore();
        } else {
            win.maximize();
        }
    });
}

app.whenReady().then(() => {
    createWindow()

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow()
    });
});


app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit()
});