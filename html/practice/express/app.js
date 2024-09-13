const express = require("express");

const app = express();
port = 80;

app.get('/', (req, res) => {
    res.send("this is my first website.");
});

app.get('/', (req, res) => {
    res.send("this is my first website.");
});

app.listen(port, () => {
    console.log(`hello world ${port}`);
})