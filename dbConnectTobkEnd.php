<?php
// Define database connection variables
$servername = "localhost";
$username = "root";
$password = "yourpassword";
$dbname = "attendance";

// Create connection
$conn = new mysqli($localhost, $root, $password, $attendance);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
// Query attendance list table
$sql = "SELECT * FROM attendance_list";
$result = $conn->query($sql);

// Display attendance list data
if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
    echo "ID: " . $row["id"]. " - Name: " . $row["name"]. " - Status: " . $row["status"]. "<br>";
  }
} else {
  echo "0 results";
}

// Close database connection
$conn->close();
?>




