<?php

include '../components/connect.php';

if(isset($_POST['submit'])){

   $t_email = $_POST['t_email'];
   $t_email = filter_var($t_email, FILTER_SANITIZE_STRING);
   $t_pass = sha1($_POST['t_pass']);
   $t_pass = filter_var($t_pass, FILTER_SANITIZE_STRING);

   $select_teacher = $conn->prepare("SELECT * FROM `teacher` WHERE t_email = ? AND t_password = ? LIMIT 1");
   $select_teacher->execute([$t_email, $t_pass]);
   $row = $select_teacher->fetch(PDO::FETCH_ASSOC);
   
   if($select_teacher->rowCount() > 0){
     setcookie('t_id', $row['t_Id'], time() + 60*60*24*30, '/');
     header('location:dashboard.php');
   }else{
      $message[] = 'incorrect email or password!';
   }

}

?>

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Login</title>

   <!-- font awesome cdn link  -->
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css">

   <!-- custom css file link  -->
   <link rel="stylesheet" href="../css/admin_style.css">
   <link rel="stylesheet" href="../css/style.css">

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

   <form action="" method="post" enctype="multipart/form-data" class="login">
      <h3>welcome back!</h3>
      <p>your email <span>*</span></p>
      <input type="email" name="t_email" placeholder="enter your email" maxlength="20" required class="box">
      <p>your password <span>*</span></p>
      <input type="password" name="t_pass" placeholder="enter your password" maxlength="20" required class="box">
      <p class="link">don't have an account? <a href="Teacher_register.php">register new</a></p>
      <input type="submit" name="submit" value="login now" class="btn">
   </form>

</section>

<!-- registe section ends -->

<!-- custom js file link  -->
<script src="js/script.js"></script>
        
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