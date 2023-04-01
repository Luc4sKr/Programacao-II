const { app, BrowserWindow } = require("electron");

let mainWindow;

app.on("ready", () => {

    mainWindow = new BrowserWindow({
        width: 900,
        height: 500,
        resizable: false
    });

    mainWindow.loadURL(`File://${__dirname}/index.html`);

});
