function validarNombre(){
    var nom = document.getElementById("txtnombre").value;
    var largo = nom.trim().lenght;
    if(largo>=3 && largo<=80){
        return true;
    } else {
        alert("no puede haber espacios en blanco en el nombre");
        return false;
    }
} 

function validarApellido(){
    var nom = document.getElementById("txtApellido").value;
    var largo = nom.trim().lenght;
    if(largo>=3 && largo<=80){
        return true;
    } else {
        alert("no puede haber espacios en blanco apellido");
        return false;
    }
}
function validarTodo(){ /*metodo que que llamara a los otra validaciones, si hay algo que tenga malo va a enviar un false*/
    var resp;

    resp=validarNombre();
    if (resp == false){
        return false;
    }

    resp=validarApellido();
    if (resp == false){
        return false;
    }


    return true;
}