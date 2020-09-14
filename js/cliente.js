class cliente {
    rut;
    nombre;
    edad;
    //de esta clase. tome la propiedad edad y en ella guarde la edad
    setRut(rut){this.rut=rut;}
    setNombre(nombre){this.nombre=nombre;}
    setEdad(edad){this.edad=edad;}
    //muestra el return 
    getRut(){return this.rut;}
    getNombre(){return this.nombre;}
    getEdad(){return this.edad;}

    imprimir(){
        return "Rut:"+this.rut+ "Nombre:" +this.nombre +
         "Edad:" + this.edad;
    }
}