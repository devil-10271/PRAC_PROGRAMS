const fs=require('fs');
let a=fs.readFile('64.txt','utf-8',(err,dat=123) =>{
    console.log('hello world\n',err,'\n',dat,'\n');
});
console.log('hello');