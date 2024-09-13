const http = require('http');
const fs = require('fs');

const fileread = fs.readFileSync('30.html');

const server=http.createServer(( req,res)=>{
    res.writeHead(200,{'Content-type':'text/html'});
    res.end(fileread);
});

server.listen(80,'127.0.0.7',()=>{
    console.log('hey i am on 127.0.0.7');
});