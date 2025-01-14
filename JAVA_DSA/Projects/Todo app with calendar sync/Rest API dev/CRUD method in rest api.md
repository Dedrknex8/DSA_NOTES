1. Create

```node
app.get('/',(req,res) =>{

    res.json({

        messsage : "Welcome to book store api"

    })

})

// Get all books

app.get('/books',(req,res) =>{

    res.json(books)

});

//Get single books

app.get('/book/:id' ,(req,res) =>{

   const book = books.find(item => item.id === parseInt(req.params.id));

   if(book){

    res .status(200).json(book);

   }else{

    res.status(404).json({

        messsage : "Product not found use correct id"

    })

   }

})
```

3. update
```node
//POST METHOD TO GET NEW BOOKS

  

app.post('/add',(req,res)=>{

    const newBook = {

        id : books.length + 1,

        title : `Book ${books.length+1}`

    }

    books.push(newBook);

    res.status(200).json(newBook);

})
```