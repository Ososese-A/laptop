const webSocket = require('ws')
const server = new WebSocke.Server({ port: '8000' })

server.on('connection', socket => {
    socket.on('message', message => {
        socket.send(`Roger that! ${message}`);
    });
});