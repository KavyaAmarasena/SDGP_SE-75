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
        //save to database
        $user_Id = random_num(20);
        $query = "insert into users (user_Id, User_name, password) values ($user_Id, $User_name, $password)";
        
        mysqli_query($con, $query);
        
        header("Location: login.php");
        die;
    }
    else
    {
        echo "Please enter some valid information!"
    }
}

?>

<!DOCTYPE html>
<html>
    <head>
        <title>Signup</title>
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
                
                <div style="font-size: 20px; margin: 10px; color:white; ">Signup</div>
                
                <input id="text" type="text" name="Use_name"><br><br>
                <input id="text" type="password" name="password"><br><br>
                
                <input id="button" type="submit" value="Signup"><br><br>
                
                <a href="login.php">Login</a><br><br>
                
            </form>
        </div>
    
    </body>
</html>