// console.log('Hello world');
// const mod=require();
// let a=mod.readFilesync('64.txt','utf-8');
// console.log(a);

const fs = require('fs');
const text = fs.readFileSync(`64.txt`, `utf-8`);
console.log(text);

console.log(`this is createing a new file...`);
a="Hello my name is sahil....";
fs.writeFileSync("64_1.txt", a);
