const baseUrl = `${window.location.protocol}//${window.location.host}`;



if (window.screen.width > 450) {
    localStorage.setItem('isOpenSidebar', true)
} else {
    localStorage.removeItem('isOpenSidebar')
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function formatPrice(value) {
    let formatting_options = {
        style: 'currency',
        currency: 'COP',
        minimumFractionDigits: 2,
     }
    let dollarString = new Intl.NumberFormat('es-CO', formatting_options );
    let finalString = dollarString.format(value);
    return  finalString;
}

function calcularDigitoVerificacion(myNit) {
    var vpri,
        x,
        y,
        z;

    // Se limpia el Nit
    myNit = myNit.replace(/\s/g, ""); // Espacios
    myNit = myNit.replace(/,/g, ""); // Comas
    myNit = myNit.replace(/\./g, ""); // Puntos
    myNit = myNit.replace(/-/g, ""); // Guiones

    // Se valida el nit
    if (isNaN(myNit)) {
        return "";
    };

    // Procedimiento
    vpri = new Array(16);
    z = myNit.length;

    vpri[1] = 3;
    vpri[2] = 7;
    vpri[3] = 13;
    vpri[4] = 17;
    vpri[5] = 19;
    vpri[6] = 23;
    vpri[7] = 29;
    vpri[8] = 37;
    vpri[9] = 41;
    vpri[10] = 43;
    vpri[11] = 47;
    vpri[12] = 53;
    vpri[13] = 59;
    vpri[14] = 67;
    vpri[15] = 71;

    x = 0;
    y = 0;
    for (var i = 0; i < z; i++) {
        y = (myNit.substr(i, 1));
        x += (y * vpri[z - i]);   
    }
    y = x % 11;

    return (y > 1) ? 11 - y : y;
}

/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openNav() {
    var isOpenSidebar = localStorage.getItem('isOpenSidebar')

    if (!isOpenSidebar) {
        document.getElementById("linebar").style.left = "-31rem";
        document.getElementById("mySidenav").style.left = "0px";
        document.getElementById("main").style.marginLeft = "250px";
        localStorage.setItem('isOpenSidebar', true)
    } else {
        closeNav()
    }
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
    document.getElementById("linebar").style.left = "-2000rem";
    document.getElementById("mySidenav").style.left = "-250px";
    document.getElementById("main").style.marginLeft = "0";
    localStorage.removeItem('isOpenSidebar')
}


function password_show_hide() {
    var x = document.getElementById("id_password");
    var show_eye = document.getElementById("show_eye");
    var hide_eye = document.getElementById("hide_eye");
    hide_eye.classList.remove("d-none");
    if (x.type === "password") {
        x.type = "text";
        show_eye.style.display = "none";
        hide_eye.style.display = "flex";
    } else {
        x.type = "password";
        show_eye.style.display = "flex";
        hide_eye.style.display = "none";
    }
}

function cleanDocFormFields(idForm) {

    const form = document.getElementById(idForm)

    for (const element of form.elements) {

        let elementTagName=element.tagName.toLowerCase()
        
        if (elementTagName === 'input' || elementTagName==='select' || elementTagName==='textarea') {

            element.value=''
            
            //para los select que son controlados por la libreria select2
            if(element.classList.contains('select2-hidden-accessible')){
                $(`#${element.id}`).val('');
                $(`#${element.id}`).trigger('change');
            }
        }
    }

}

