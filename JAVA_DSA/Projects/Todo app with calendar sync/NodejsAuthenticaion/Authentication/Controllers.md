> this is for the auth controllers

```node
  
  

//REGISTER CONTROLLER

const registerUser = async(req,res)=>{

    try {

    } catch (error) {

        console.log(error);

        res.status(500).json({

            success : false,

            messgae: "Something went wrong"

        });

    }

}

  

//LOGIN CONTROLLERS for this find one unique

// attribute in your model.js like usernmae or email field

const loginUser = async(req,res)=>{

    try {

    } catch (error) {

        console.log(error);

        res.json({

            success : false,

            messgae : "something went worng"

        });

    }

}

  

module.exports  = (registerUser,loginUser);
```