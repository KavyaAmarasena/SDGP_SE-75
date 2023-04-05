<?php

include '../components/connect.php';

if(isset($_POST['submit'])){

   $t_id = unique_id();
   $t_fname = $_POST['t_fname'];
   $t_fname = filter_var($name, FILTER_SANITIZE_STRING);
   $t_lname = $_POST['t_lname'];
   $t_lname = filter_var($name, FILTER_SANITIZE_STRING);
   $t_email = $_POST['t_email'];
   $t_email = filter_var($email, FILTER_SANITIZE_STRING);
   $t_pass = sha1($_POST['t_pass']);
   $t_pass = filter_var($pass, FILTER_SANITIZE_STRING);
   $t_cpass = sha1($_POST['t_cpass']);
   $t_cpass = filter_var($cpass, FILTER_SANITIZE_STRING);

   $t_image = $_FILES['t_image']['t_fname'];
   $t_image = filter_var($image, FILTER_SANITIZE_STRING);
   $ext = pathinfo($image, PATHINFO_EXTENSION);
   $rename = unique_id().'.'.$ext;
   $image_size = $_FILES['t_image']['size'];
   $image_tmp_name = $_FILES['t_image']['tmp_name'];
   $image_folder = '../uploaded_files/'.$rename;

   $select_student = $conn->prepare("SELECT * FROM `teacher` WHERE t_email = ?");
   $select_teacher->execute([$t_email]);
   
   if($select_teacher->rowCount() > 0){
      $message[] = 'email already taken!';
   }else{
      if($pass != $cpass){
         $message[] = 'confirm passowrd not matched!';
      }else{
         $insert_teacher = $conn->prepare("INSERT INTO `teacher`(t_Id,t_fname,t_lname,t_email, t_password, t_image) VALUES(?,?,?,?,?,?)");
         $insert_teacher->execute([$t_id, $t_name, $t_email, $t_cpass, $rename]);
         move_uploaded_file($image_tmp_name, $image_folder);
         $message[] = 'new teacher registered! please login now';
      }
   }

}

?>

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>register</title>

   <!-- font awesome cdn link  -->
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css">

   <!-- custom css file link  -->
   <link rel="stylesheet" href="../css/admin_style.css">

</head>
<body style="padding-left: 0;">

<?php
if(isset($message)){
   foreach($message as $message){
      echo '
      <div class="message form">
         <span>'.$message.'</span>
         <i class="fas fa-times" onclick="this.parentElement.remove();"></i>
      </div>
      ';
   }
}
?>

<!-- register section starts  -->

<section class="form-container">

   <form class="register" action="" method="post" enctype="multipart/form-data">
      <h3>GET START WITH LARNLY</h3>
      <div class="flex">
         <div class="col">
            <p>First name <span>*</span></p>
            <input type="text" name="t_fname" placeholder="Enter your first name" maxlength="50" required class="box">
            <p>Username <span>*</span></p>
            <input type="text" name="t_username" placeholder="Enter your username" maxlength="20" required class="box">
            <p>Password <span>*</span></p>
            <input type="password" name="t_pass" placeholder="Enter your password" maxlength="20" required class="box">
         </div>
         <div class="col">
            <p>Last name <span>*</span></p>
            <input type="text" name="t_lname" placeholder="Enter your last name" maxlength="50" required class="box">
            <p> Email <span>*</span></p>
            <input type="email" name="t_email" placeholder="Enter your email" maxlength="20" required class="box">
            <p>confirm password <span>*</span></p>
            <input type="password" name="t_cpass" placeholder="confirm your password" maxlength="20" required class="box">
         </div>
      </div>
      <p>select pic <span>*</span></p>
      <input type="file" name="t_image" accept="image/*" required class="box">
      <p class="link">Already have an account? <a href="login.php">Sign In</a></p>
      <input type="submit" name="submit" value="Sign Up" class="btn">
   </form>

</section>

<!-- registe section ends -->

<script>

let darkMode = localStorage.getItem('dark-mode');
let body = document.body;

const enabelDarkMode = () =>{
   body.classList.add('dark');
   localStorage.setItem('dark-mode', 'enabled');
}

const disableDarkMode = () =>{
   body.classList.remove('dark');
   localStorage.setItem('dark-mode', 'disabled');
}

if(darkMode === 'enabled'){
   enabelDarkMode();
}else{
   disableDarkMode();
}

</script>
   
</body>
</html>