
# Date 02-02-25 || Rohit Tiwari

#### To be covered
- [x] cors
- [ ] redis

## what is CORS?

> CORS stands for cross origin resource sharing . It used allow permission for sharing resources to a domain or Ip

> It basically means allowing domain, Ip to access resources of a site like authorization.


### API Versoning

> It's a way through which a site can verify or know which verson of API a particular want to access

## apiVersoning.js

```javascript
// 3 Types of apiVersioning urlVersoning,headerVersoning,Content-typeVersoinig

const urlVersoning = (version) => (req,res,next)=>{

    if(req.path.startsWith(`/api/${version}`)){

        next();

    }else{

        res.status(404).json({

            success : false,

            message : "API version is not supported"

        });

    }

};

  

const headerVersioning = (version) => (req,res,next)=>{

    if(req.get('Accept-Version') === version){

        next();

    }else{

        res.status(404).json({

            success : false,

            message : "API version is not supported"

        });

    }

}

  

const contentTypeVersoning = (version)=>(req,res,next)=>{

    const contentType = req.get('Content-Type');

    if(contentType && contentType.includes(`application/vndd.api.${version}+json`));

};

  

module.exports = { urlVersoning,headerVersioning,contentTypeVersoning }

```

Use this on server.js `app.use('/api/v1',urlVersoining(v1));`


## Rate limit 

> Rate limit is way to limit a user by allowing a certain amount of request per User. Example : when trying to login with wrong password after a certain request it says too many request try again later .


```node
const rateLimit = require('express-rate-limit');

  

const createBasicRateLimiter = (maxRequest, time)=>{

    return rateLimit({

        max : maxRequest,

        windowMs : time,

        message : "Too many request ! Try again later",

        standardHeaders  :true,

        legacyHeaders : false

    })

}

  

module.exports = { createBasicRateLimiter};
```



## Error handling

```node

class APIError extends Error {

    constructor(message,statusCode){

        super(message);

        this.statusCode = statusCode;

        this.name = "APIError"; // set the error type to APIError

    }

}

const asyncHandler =(fn)=>(req,res,next) =>{

    Promise.resolve(fn(req,res,next)).catch((err) => next(err));

}

  

const globalErrorHandler = (err,req,res,next) =>{

    console.error(err.stack); //log the error stack

    if(err instanceof APIError){

        return res.status(err.statusCode).json({

            status : 'error',

            mess  : err.message

        })

    }

    //Similarly can check validation error

    else if(err.name === 'validationError'){

        return res.status(400).json({

            status : 'error',

            mess  : err.message

        })

    }

    else{

        return res.status(500).json({

            status : 'error',

            mess  : 'An unexpected error occured'

        })

    }

}

  

module.exports = {APIError,asyncHandler,globalErrorHandler}
```

