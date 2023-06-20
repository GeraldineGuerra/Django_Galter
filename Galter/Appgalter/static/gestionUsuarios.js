document.addEventListener("DOMContentLoaded", function(){

    document.getElementById("frmInsertar").addEventListener("submit", function(event){
        event.preventDefault();

        var data={
            codi_usuario:document.getElementById("codi_usuario").value,
            nombre_usuario:document.getElementById("nombre_usuario").value,
            correo_usuario:document.getElementById("correo_usuario"). value,
            pass_ususario:document.getElementById("pass_ususario").value,
            tipo_usuario:document.getElementById("tipo_usuario").value
        };

        var jsonData=JSON.stringify(data);
        fetch("http://127.0.0.1:8000/insertarUsu/",{
            method:'POST',
            body:jsonData,
            headers:{
                "Content-Type":"Appgalter/json"
            }
        })

        .then(response => response.json())
        .then(datos=>{
            console.log(datos)

        })

        .catch(console.error())
        


    });



});