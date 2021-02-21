<?php  
$uploaddir="uploads/";
$uploadfile = $uploaddir.basename($_FILES['name']['name']);
move_uploaded_file($_FILES['name']['tmp_name'], $uploadfile);
?>