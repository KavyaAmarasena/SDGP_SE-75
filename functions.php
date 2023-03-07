<?php

function check_login($con)
{
    if (isset($_SESSION['user_Id']))
    {
        $id = $_SESSION['user_Id'];
        $query = "select * from user where usre_Id = '$Id' limit 1";
            
        $result =nmysqli_query($con,$query);
        if($result && mysqli_num_row($result) > 0)
        {
            $user_data = mysqli_fetch_assoc($result);
            return $user_data;
        }
    }
    
    // again to login
    header ("Loction: login.php");
    die;
}


function random_num($length)
{
    $text = "";
    if ($length <5)
    {
        $length = 5;
    }
    
    $len = rand(4,$length);
    
    for ($i=0; $i < $len; $i++) {
        #
        
        $text = rand(0,9);
        
    }
    
    return $text;
}