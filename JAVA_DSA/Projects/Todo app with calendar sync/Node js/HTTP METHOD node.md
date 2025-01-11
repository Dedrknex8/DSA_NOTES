
> Http is a method in node js to create a http sevrer backend realted things like handling api calls and other

```node
const http = require('http');

//CREATESERVER IS A METHOD TO CREATE A SERVER

const server = http.createServer((req,res)=>{

    console.log(req, 'req');

  
	res.send('hello world);

});

  

const port = 2929; //create a listnening port

  

server.listen(port, ()=>{

    console.log(`server running on ${port}`)

}); //server.listen is a method to listen
```

