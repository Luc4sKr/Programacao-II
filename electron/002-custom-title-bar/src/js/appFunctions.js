const { ipcRenderer } = require("electron");
const ipc = ipcRenderer;

///// close app
document.querySelector("#close-btn").addEventListener("click", () => {
    ipc.send("closeApp");
});

///// minimize app
document.querySelector("#minimize-btn").addEventListener("click", () => {
    ipc.send("minimizeApp");
});

///// maximize app
document.querySelector("#maximize-btn").addEventListener("click", () => {
    ipc.send("maximizeRestoreApp");
});
