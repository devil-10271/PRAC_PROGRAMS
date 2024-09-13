// console.log("hello world");
const http = require('http');

const hostname = '127.0.0.1';

const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    res.end(`<DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ANIMATION</title>

        <style>
            body {
                background: #000;
                margin: 0%;
                padding: 0%;
            }

            .main {
                background-color: grey;
                margin: 10px;
                border-radius: 10px;
            }

            .box {
                background: rgb(255, 255, 255);
                width: 0px;
                height: 25px;
                animation-name: w1;
                animation-duration: 5s;
                animation-iteration-count: infinite;
                animation-fill-mode: forwards;
                border-radius: 10px;
                animation-direction: reverse;

            }

            .main2 {
                background: #fff;
                margin: 10px;
                border-radius: 10px;
            }

            #box {
                background: grey;
                width: 250px;
                height: 25px;
                animation-name: w1;
                animation-duration: 10s;
                animation-iteration-count: infinite;
                animation-fill-mode: forwards;
                border-radius: 10px;
                animation-direction: reverse;

            }


            @keyframes w1 {
                0% {
                    width: 0px;
                }

                10% {
                    width: 100%;
                }

                20% {
                    width: 0px;
                }

                30% {
                    width: 100%;
                }

                40% {
                    width: 0px;
                }

                50% {
                    width: 100%;
                }
                60% {
                    width: 0px;
                }

                70% {
                    width: 100%;
                }

                80% {
                    width: 0px;
                }

                90% {
                    width: 100%;
                }
                100% {
                    width: 100%;
                }
            }
        </style>
    </head>

    <body>
        <div class="main">
            <div class="box"></div>
        </div>

        <div class="main2">
            <div id="box"></div>
        </div>

        <div class="main">
            <div class="box"></div>
        </div>

        <div class="main2">
            <div id="box"></div>
        </div>

        <div class="main">
            <div class="box"></div>
        </div>

        <div class="main2">
            <div id="box"></div>
        </div>

        <div class="main">
            <div class="box"></div>
        </div>

        <div class="main2">
            <div id="box"></div>
        </div>
        <div class="main">
            <div class="box"></div>
        </div>

        <div class="main2">
            <div id="box"></div>
        </div>

        <div class="main">
            <div class="box"></div>
        </div>

        <div class="main2">
            <div id="box"></div>
        </div>

        <div class="main">
            <div class="box"></div>
        </div>

        <div class="main2">
            <div id="box"></div>
        </div>

        <div class="main">
            <div class="box"></div>
        </div>

        <div class="main2">
            <div id="box"></div>
        </div>
    </body>

    </html>`);
});

server.listen(port, hostname, () => {
    console.log(`server running at http://${hostname}:${port}/`);
});