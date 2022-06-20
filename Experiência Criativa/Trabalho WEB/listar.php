<?php


    $con = mysqli_connect("localhost", "root", "", "cadastro");

    $resultado = mysqli_query($con, "SELECT * FROM formulario");

    $contador = 0;
    while($linha = mysqli_fetch_assoc($resultado)){
        
        $retorno[$contador]["nome"] = $linha["nome"];
        $retorno[$contador]["email"] = $linha["email"];
        $contador++;
    }
echo json_encode($retorno);
    

?>