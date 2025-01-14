1. GET

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

2. Create
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

3. Update / PUT METHOD
```node
//Update the book titile

app.put('/update/:id',(req,res) =>{

    const findBook = books.find(booksItems => booksItems.id === parseInt(req.params.id))

  

    if(findBook){

        findBook.title = req.body.title || findBook.title

  

        res.status(200).json({

            messsage  : `book with ${req.params.id} updated successfully`,

            data : findBook

        });

    }else{

        res.status(404).json({

            messsage : `cannot find book with ${findBook.id}`

        })

    }

})
```

4. Delete 
```node
//DELETE FUNCTION

app.delete('/delete/:id',(req,res) =>{

    const deleteBook = books.findIndex(deleteItem => deleteItem.id === parseInt(req.params.id))

  

    if(deleteBook !== -1){

        const deletedbook  =books.splice(deleteBook,1);

        res.status(200).json(

            {

                message : `book deleted successfully with id ${req.params.id}`,

                data : deletedbook[0]

            }

        )

    }else{

        req.status(404).json({

            messsage : "cannot finf book"

        })

    }

})
```