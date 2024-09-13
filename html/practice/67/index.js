const fs = require('fs');
const http = require('http');
const { url } = require('inspector');

const hostname = '127.0.0.1';
const port = 8000;

const home = fs.readFileSync('index.html');
const about = fs.readFileSync('about.html');
const serv = fs.readFileSync('services.html');
const cont = fs.readFileSync('contact.html');

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    res.end(home);

    if (url == 'index.html') {
        res.end(home);
    }
    else if (url == 'http://127.0.0.1:8000/services.html') {
        res.end(serv);
    }
    // else if (url == 'about.html') {
    //     res.end(about);
    // }
    // else {
    //     res.end(serv);
    // }
    // else {
    //     res.end('<h1> 404 padge is not found.');
    // }


});

server.listen(port, hostname, () => {
    console.log(`Server is running on http://${hostname}:${port}`);
});