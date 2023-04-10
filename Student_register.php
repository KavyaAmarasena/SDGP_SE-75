<?php

include '../components/connect.php';

if(isset($_POST['submit'])){

   $id = unique_id();
   $s_fname = $_POST['s_fname'];
   $s_fname = filter_var($s_fname, FILTER_SANITIZE_STRING);
   $s_lname = $_POST['s_lname'];
   $s_lname = filter_var($s_lname, FILTER_SANITIZE_STRING);
   FILTER_SANITIZE_STRING);
   $s_email = $_POST['s_email'];
   $s_email = filter_var($s_email, FILTER_SANITIZE_STRING);
   $s_pass = sha1($_POST['s_pass']);
   $s_pass = filter_var($s_pass, FILTER_SANITIZE_STRING);
   $s_cpass = sha1($_POST['s_cpass']);
   $s_cpass = filter_var($s_cpass, FILTER_SANITIZE_STRING);

   $s_image = $_FILES['s_image']['s_fname'];
   $s_image = filter_var($s_image, FILTER_SANITIZE_STRING);
   $ext = pathinfo($s_image, PATHINFO_EXTENSION);
   $s_rename = unique_id().'.'.$ext;
   $image_size = $_FILES['s_image']['size'];
   $image_tmp_name = $_FILES['s_image']['tmp_name'];
   $image_folder = '../uploaded_files/'.$rename;

   $select_student = $conn->prepare("SELECT * FROM `students` WHERE s_email = ?");
   $select_student->execute([$s_email]);
   
   if($select_student->rowCount() > 0){
      $message[] = 'email already taken!';
   }else{
      if($pass != $cpass){
         $message[] = 'confirm passowrd not matched!';
      }else{
         $insert_student = $conn->prepare("INSERT INTO `students`(s_Id, s_fname,s_lname, s_email, s_password, s_image) VALUES(?,?,?,?,?,?)");
         $insert_student->execute([$s_id, $s_fname,$s_lname, $s_email, $s_cpass, $s_rename]);
         move_uploaded_file($image_tmp_name, $image_folder);
         $message[] = 'new student registered! please login now';
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
            <input type="text" name="s_fname" placeholder="Enter your first name" maxlength="50" required class="box">
            <p>Username <span>*</span></p>
            <input type="text" name="s_username" placeholder="Enter your username" maxlength="20" required class="box">
            <p>Password <span>*</span></p>
            <input type="password" name="s_pass" placeholder="Enter your password" maxlength="20" required class="box">
         </div>
         <div class="col">
            <p>Last name <span>*</span></p>
            <input type="text" name="s_lname" placeholder="Enter your last name" maxlength="50" required class="box">
            <p>Email <span>*</span></p>
            <input type="email" name="s_email" placeholder="Enter your email" maxlength="20" required class="box">
            <p>Confirm password <span>*</span></p>
            <input type="password" name="s_cpass" placeholder="Confirm your password" maxlength="20" required class="box">
         </div>
      </div>
      <p>Select pic <span>*</span></p>
      <input type="file" name="s_image" accept="image/*" required class="box">
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