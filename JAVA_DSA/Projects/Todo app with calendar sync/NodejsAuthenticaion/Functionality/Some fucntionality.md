# Date 22-01-25 || Rohit Tiwari

> Here will cover about deleting the file changing the passwd

## Change password functionality

```node 
//CHANGE PASSWD

const changePassword = async(req,res)=>{

    try {

        const userId = req.userInfo.userId;

        //GET OLD AND NEW PASSWD FROM FRONTEND  

        const {oldPassword,newPasword} = req.body;

  

        //find the current user login info

        const user = await Users.findById(userId);

  

        if(!user){

            return res.status(400).json({

                message : "User doesn't exist.Please register first"

            })

        }

        //CHECK IF OLD PASSWORD IS CORRECT old passwd => user.passwd && and oldpasswd -> req.body{userInput}

        const isOldPasswordValid = await bcrypt.compare(oldPassword,user.password);

  

        if(!isOldPasswordValid){

            return res.status(400).json({

                sucess :false,

                messgae : "Credential don't match"

            })

        }


        //HASH THE NEW PASSWD

        const salt = await bcrypt.genSalt(10);

        const newHashedPassword = await bcrypt.hash(newPasword,salt);

        //update the new password

        user.password = newHashedPassword;

        await user.save();//Imp step ()

  

        res.status(200).json({

            success  :true,

            message : "Password changed successfully"

        });

    } catch (error) {

        console.log(error);

        res.status(500).json({

            success : false,

            message : "Some went wrong chaning passwd"

        });

    }
```

## Delete the uploaded file

> To delete that file we need to delete it from the cloudinary and mongoDB databases


```node
const deleteImageController = async(req,res)=>{

    try {

        const getCurrentImageToBEDeleted = req.params.id;

        const userId = req.userInfo.userId;

        //GET THE CURRENT IMAGE TO DELETE

        const image = await Image.findById(getCurrentImageToBEDeleted);

  

        if(!image){

            return res.status(400).json({

                success : false,

                messasge : "Can't find image.Please check the image Id to be deleted"

            })

        };

        // Check if this image is uploaded by the current USer

        if(image.uploadedBy.toString() !== userId){

            return res.status(403).json({

                success : false,

                messasge : "Unauthorized access"

            })

        }

  

        // Delete this imageFrom cloudinary

        await cloudinary.uploader.destroy(image.publicId);

  

        //delete this image from mongo db

        await Image.findByIdAndUpdate(getCurrentImageToBEDeleted);

  

        // //update and save in mongo db

        // await image.save();

  

        res.status(200).json({

            success: true,

            message : "Image deleted sucesfully"

        });

  
  

    } catch (error) {

        console.log(error);

        res.status(500).json({

            success : false,

            messasge : "Some went wrong in deleting image"

        })

    }

}
```

## Image-route

```node
router.delete('/:id', authmiddleware, isAdminUser, deleteImageController);
```