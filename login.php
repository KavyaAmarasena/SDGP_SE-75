<?php

session_start();

include("connection.php");
include("functions.php");

if($_SERVER['REQUEST_METHOD'] == "POST")
{
    $User_name = $_POST['User_name'];
    $password = $_POST['password'];
    
    if(!empty($User_name) && !empty($password) && !is_numeric($User_name))
    {
        //read from database
        $user_Id = random_num(20);
        $query = "select * from users whereUser_name = '$User_name' limit 1 ";
        
        $result = mysqli_query($con, $query);
        
    if($result && mysqli_num_rows ($result) > 0)
    {
        $user_data = mysqli_fetch_assoc($result);
        if($user_data['password'] === $password)
        {
            $_SESSION['user_Id'] = $user_data['user_Id'];
            header("Location: index.php");
             die;
        }
    }
        
       
    }
    
    echo "Wrong username or password!"
    
    else
    {
        echo "Please enter some valid information!"
    }
}


?>

<!DOCTYPE html>
<html>
    <head>
        <title>Login</title>
    </head>
    
    <body>
        
        <style type="text/css">
            
            #text {
                height: 25px;
                border-radius: 5px;
                padding: 4px;
                border: solid thin #aaa;
                width: 100%;
            }
            
            #button {
                padding: 10px;
                width: 100px;
                color: white;
                background-color: lightblue;
                border: none;
            }
            
            #box {
                background-color: grey;
                margin: auto;
                width: 300px;
                padding: 20px;
            }
        </style>
        
        <div Id="box">
            
            <form method="post">
                
                <div style="font-size: 20px; margin: 10px; color:white; ">Login</div>
                
                <input id="text" type="text" name="Use_name"><br><br>
                <input id="text" type="password" name="password"><br><br>
                
                <input id="button" type="submit" value="Login"><br><br>
                
                <a href="signup.php">Signup</a><br><br>
                
            </form>
        </div>
    
    </body>
</html>