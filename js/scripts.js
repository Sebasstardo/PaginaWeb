function validarRut(){
    // De este documento quiero el elemento que tenga este ID, de este ID quiero su valor
  var rut =document.getElementById("txtRut").value;
  if (rut.length!=10){
      alert("rut incompleto");
      return false;
  }
  var num=3; //secuencia
  var suma=0;
   for (let index = 0; index < 8; index++) {             
      var carac= rut.slice(index, index + 1); // slice permite recuperar un texto, es 1 mas lo que quiero hacia el lado
      suma = suma + (carac*num);
      num= num - 1;
      if (num == 1){
          num = 7;
      }
   }
   var resto = suma % 11;
   var dv= 11 - resto;
   if(dv > 9){
       if(dv==10){
          dv='K';                                   
       } else {
          dv=0;
       }
   }                    
  var dv_usuario= rut.slice(-1).toUpperCase();
  if(dv!=dv_usuario){
      alert("rut incorrecto");
      return false;
  }
  return true;
}
function validarFecha(){
    var fechaForm = document.getElementById("txtfecha").value; 
     var fechaSistema = new Date();
     ///////////////////////////////////////////
     var ano = fechaForm.slice(0, 4);   
     var mes = fechaForm.slice(5, 7);  
     var dia = fechaForm.slice(8, 10); 
     /////////////////////////////////////////
     var fechaMia = new Date (ano, (mes-1), dia);
    //////////////////////////////////////// 
    if (fechaMia > fechaSistema) {
        alert("fecha de nacimiento incorrecto");
        return false;
    }

    return true;
}
function validarTodo(){ /*metodo que que llamara a los otra validaciones, si hay algo que tenga malo va a enviar un false*/
    var resp;
    resp=validarRut();/* si la respuesta es verdadera seguira leyendo las otras*/
    if (resp==false){
        return false;
    }
    
    resp=validarFecha();
    if(resp==false){
        return false;
    }
    return true;
    


}