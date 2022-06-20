<?php
include "conexao.php"; 

$nome=$_POST['nome'];
$email=$_POST['email'];
$senha=$_POST['senha'];

$sql="INSERT INTO formulario(nome,email,senha) 
    Values ('$nome','$email','$senha')";

if (mysqli_query($conexao,$sql)){
    echo 'cadastrado';
}
else{
    echo'erro'.mysqli_connect_error($conexao);
}
mysqli_close($conexao);
?>