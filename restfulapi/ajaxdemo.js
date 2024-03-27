$(document).ready(function(){


    $("#ejemplo-get").click(function(){

        $.get("http://127.0.0.1:5000/getTest",function(data,status){
            $("#parrafo-1").html(data);

        });

    });
    
    $("#boton").click(function() {
        var nombre = document.getElementById('esp1').value;
        var email = document.getElementById('esp2').value;
    
        $.ajax({
            type: "post",
            url: "http://127.0.0.1:5000/postTest",
            contentType: 'application/json',
            data: JSON.stringify({
                'nombre': nombre,
                'email': email
            }),
            success: function(response) {
                alert('Data Sent: Name - ' + response.nombre + ', Email - ' + response.email);
            },
            error: function(xhr, status, error) {
                alert("Error: " + xhr.responseText);
            }
        });
    
        return false;
    });
    


});