const http = require('http');

const server = http.createServer((request, response) => {
    response.writeHead(200, { "Content-Type": "text/plain" });
    response.end("Hello there, I am Jesse. I develop softwares in Python3, HTML, JavaScript, CSS, Angular, React, Nodejs, SQL, mySQL, postgreSQL, C#, Java, Flutter and Arduino. Check out: https://github.com/jessedeveloperinvestor");
});

const port = process.env.PORT || 8080;
server.listen(port);

console.log("Server running at http://localhost:%d", port);