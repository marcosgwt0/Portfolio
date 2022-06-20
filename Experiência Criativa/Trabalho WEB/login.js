function registrar(){
    user = document.getElementById('nome').value;
    e_mail = document.getElementById('email').value;
    _senha = document.getElementById('senha').value;
    $.ajax({
        type:'POST',
        dataType:'json',
        url:'./cadastro.php',
        data: {nome:user, email:e_mail,senha:_senha},
        success: function(response){
            console.log(response);
        }
    });
}