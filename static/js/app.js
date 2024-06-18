const id_fecha_nac = document.getElementById("id_fecha_nac");
const edad = document.getElementById("edad");

const calcularEdad=(id_fecha_nac) => {
    const fechaActual = new Date();
    const anoActual = parseInt(fechaActual.getFullYear());
    const mesActual = parseInt(fechaActual.getMonth()) + 1;
    const diaActual = parseInt(fechaActual.getDate());

    const anoNacimiento = parseInt(String(id_fecha_nac).substring(0, 4));
    const mesNacimiento = parseInt(String(id_fecha_nac).substring(5, 7));
    const diaNacimiento = parseInt(String(id_fecha_nac).substring(8, 10));

    let edad = anoActual - anoNacimiento;
    if (mesActual < mesNacimiento) {
        edad=edad-1;
    } else if (mesActual === mesNacimiento) {
        if (diaActual < diaNacimiento) {
            edad= edad-1;
        }
    }
    return edad;
};

window.addEventListener('load',function () {
    id_fecha_nac.addEventListener('change', function () {
        if (this.value) {
            edad.innerText = 'Edad: ${calcularEdad(this.value)} años';
        }
    });
});