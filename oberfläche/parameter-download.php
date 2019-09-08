<?php
$con=mysqli_connect("localhost","datenbank","rasp","datenbank");
// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

$sql="SELECT slot, pflanze, temperatur, lichtstunden, wassermenge, luftfeuchtigkeit FROM parameter ORDER BY  slot";

if ($result=mysqli_query($con,$sql))
  {
  // Fetch one and one row
  while ($row=mysqli_fetch_row($result))
    {
        echo "$row[0] $row[1] $row[2] $row[3] $row[4] $row[5] \r\n";
    }
  // Free result set
  mysqli_free_result($result);
}

mysqli_close($con);
?> 