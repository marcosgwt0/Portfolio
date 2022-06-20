
function listar(){
    $.ajax({
        type: "GET",
        url: "listar.php",
        dataType: "json",
        success: function(retorno) {
            for (let i = 0; i <=retorno.length; i++){
                document.getElementById("mostrar").innerHTML += retorno[i]["email"] + "                                                      " + retorno[i]["nome"]+ "<br>"+"<br>";
            }
        }
    })
}