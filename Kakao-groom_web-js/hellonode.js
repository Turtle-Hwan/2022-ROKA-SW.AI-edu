/* 놀랍게도 github codespace에는 node 및 npm이 설치되어 있다.
다양한 도구가 설치된 리눅스 서버를 할당해 주는 듯하며 root 디렉토리에도 접근이 가능하다.
그렇다면 하나의 codespace로 작업하며 여러 git repo를 만들어 github에 push할 수 있지 않을까?*/


console.time('time');
const server = require('http');

server.createServer(function(req, res){
  res.writeHead(200, { 'Content-Type' : 'text/plain' });
  res.end("Hello node.js! \n");
}).listen(3000, 'localhost');

console.log('Server is running at http://localhost:3000/');
console.timeEnd('time');