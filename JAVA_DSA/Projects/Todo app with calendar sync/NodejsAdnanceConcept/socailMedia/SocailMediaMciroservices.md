
```powershell
PS D:\Cybersec\New folder\AdvanceConcepts\SocailMediaMicroservercies\identity-service> npm install dotenv express express-http-proxy cors helmet ioredis jsonwebtoken winston
```


#### Under identity-service /

```powershell
identity-services> npm i dotenv argon2 express express-rate-limit cors helmet ioredis joi jsonwebtoken mongoose rate-limit-redis winston
```



## summary of the library used

1. Joi -> used validate schema
2. agron2 -> used for hashing
3. Winston - > provide multiple loging library support
4. helmet -> Help secure Express apps by setting HTTP response headers.
5. Node rate limiter flexible -> Protect against DOs and DDos

## What is the main purpose ?

The two separate folder will communicate with each other using microservices

# Code goes here for Identity-service

> Link to github code page for better resuability


## Token Genration

```node
const jwt = require('jsonwebtoken');

const generateToken = async(user)=>{

    const accessToken = jwt.sign({

        userId :user._id,

        username : user.username,

        role : user.role,

    },process.env.JWT_Secret,{

        expiresIn :'15m' //this will expire after 15Min

    })

    //REFRESH TOKEN GENRARTE TOKEN AFTER EXPIRY WIHTOUT HAVING TO LOG IN

    const refreshToken = crypto.randomBytes(40).toString('hex'); // this will create a token

    const expiresAt = new Date();

    expiresAt.setDate(expiresAt.getDate()+7);

  

    await refreshToken.create({

        token : refreshToken,

        user : user._id,

        expiresAt

    })

    return {accessToken,refreshToken}

}

  

module.exports = generateToken
```


## how conenction is made

>Used express http proxy which is used to proxy the proxy the port or forward it and also repalced /api -> /v1 code 

```node
// create proxy

const proxyOptions = {

    proxyReqPathResolver: (req) => {

         return req.originalUrl.replace(/^\/v1/, '/api'); //this will replace api with v1 and new path as with port 3001

        // console.log("🔹 Proxying request to:", newPath);

        // return newPath;

    },      

    proxyErrorHandler : (err,res,next)=>{

        console.log(err);

        logger.error(`Proxy error ${err.message}`);

        res.status(500).json({

            success:false,

            message:`Internal Server Error err:${err.message}`

        })

    }

}

  

//setting proxy for identity service

app.use('/v1/auth',proxy(process.env.IDENTITY_SERVICE_URL,{

    ...proxyOptions,

    proxyReqOptDecorator: (proxyReqOpts,srcReq)=>{

        proxyReqOpts.headers['Content-Type']="application/json"

        return proxyReqOpts;

    },

    userResDecorator: (proxyRes,proxyResData,userReq,userRes)=>{

        logger.info(`Response recived from Identity service: ${proxyRes.statusCode} `);

        // console.log("Something wrong here");

    return proxyResData;

    },

}));

  

app.use(errorHandler);

  
app.listen(PORT,()=>{

    logger.info(`API GATEWAY IS RUNNIN ON PORT ${PORT} `);

    logger.info(`Identity service is running on ${process.env.IDENTITY_SERVICE_URL} `)

})
```