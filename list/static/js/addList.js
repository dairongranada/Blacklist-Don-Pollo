var isAdvancedUpload = function () {
  var div = document.createElement('div');
  return (('draggable' in div) || ('ondragstart' in div && 'ondrop' in div)) && 'FormData' in window && 'FileReader' in window;
}();

let draggableFileArea = document.querySelector(".drag-file-area");
let browseFileText = document.querySelector(".browse-files");
let uploadIcon = document.querySelector(".upload-icon");
let dragDropText = document.querySelector(".dynamic-message");
let fileInput = document.querySelector(".default-file-input");
let cannotUploadMessage = document.querySelector(".cannot-upload-message");
let cancelAlertButton = document.querySelector(".cancel-alert-button");
let uploadedFile = document.querySelector(".file-block");
let fileName = document.querySelector(".file-name");
let fileSize = document.querySelector(".file-size");
let progressBar = document.querySelector(".progress-bar");
let removeFileButton = document.getElementById("remove-file-button");
let uploadButton = document.getElementById("upload-button");
let fileFlag = 0;


function download(url) {
  window.location.replace(`${baseUrl}${url.replace('media','media_files')}`)
}


fileInput.addEventListener("click", () => {
  fileInput.value = '';
});

fileInput.addEventListener("change", e => {
  uploadIcon.innerHTML = 'check_circle';
  dragDropText.innerHTML = '¡Archivo listo!';
  fileName.innerHTML = fileInput.files[0].name;
  fileSize.innerHTML = (fileInput.files[0].size / 1024).toFixed(1) + " KB";
  uploadedFile.style.cssText = "display: flex;";
  progressBar.style.width = 0;
  fileFlag = 0;

});

cancelAlertButton.addEventListener("click", () => {
  cannotUploadMessage.style.cssText = "display: none;";
});

if (isAdvancedUpload) {
  ["drag", "dragstart", "dragend", "dragover", "dragenter", "dragleave", "drop"].forEach(evt =>
      draggableFileArea.addEventListener(evt, e => {
          e.preventDefault();
          e.stopPropagation();
      })
  );

  ["dragover", "dragenter"].forEach(evt => {
      draggableFileArea.addEventListener(evt, e => {
          e.preventDefault();
          e.stopPropagation();
          uploadIcon.innerHTML = 'file_download';
          dragDropText.innerHTML = '¡Suelta tu archivo aquí!';

      });
  });

  draggableFileArea.addEventListener("drop", e => {
      uploadIcon.innerHTML = 'check_circle';
      dragDropText.innerHTML = '¡Archivo listo!';

      let files = e.dataTransfer.files;
      fileInput.files = files;

      fileName.innerHTML = files[0].name;
      fileSize.innerHTML = (files[0].size / 1024).toFixed(1) + " KB";
      uploadedFile.style.cssText = "display: flex;";
      progressBar.style.width = 0;
      fileFlag = 0;
  });
}

removeFileButton.addEventListener("click", () => {
  uploadedFile.style.cssText = "display: none;";
  fileInput.value = '';
  uploadIcon.innerHTML = 'file_upload';
  dragDropText.innerHTML = 'Arrastra y suelta el archivo aquí';

});


uploadButton.addEventListener("click", () => {

  let isFileUploaded = fileInput.value;
  console.log(isFileUploaded)
  
  if (isFileUploaded != '') {
      uploadButton.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i>`;
      removeFileButton.style.cssText = "display: none;";

      let fd = new FormData()


      fd.append('LISTA_INTERNA', fileInput.files[0])
      console.log(isFileUploaded)

      $.ajax({
          type: "POST",
          contentType: 'multipart/form-data',
          headers: { "Accepts": "text/plain; charset=utf-8", "X-CSRFToken": getCookie('csrftoken') },
          url: `${baseUrl}/api/cargar-excel/`,
          processData: false, 
          contentType: false,
          data: fd,
      }).done(function (data) {
        console.log(data);
          Swal.fire({
              title: data.warning == true ? 'warning' :'Exito',
              text:  data.msg, 
              icon: data.warning == true ? 'warning' :'success',
              confirmButtonColor: '#3085d6',
              confirmButtonText: 'Ok',
              allowOutsideClick: false
          }).then((result) => {
              if (result.isConfirmed) {
                  uploadedFile.style.cssText = "display: none;";
                  fileInput.value = '';
                  uploadIcon.innerHTML = 'file_upload';
                  dragDropText.innerHTML = 'Arrastra y suelta el archivo aquí';  
              }
          })
      }).fail(function (data) {
          
          var res = data.responseJSON;
          var status = data.status
          var text = 'Ha ocurrido un error'


          console.log(res);

          if (status === 500) {
              text = 'Ha ocurrido un error inesperado, por favor contactar a soporte'
          } else if (status === 403 || status === 401) {
              text = "Usted no se encuentra autorizado para realizar esta operación";
          } else if (status === 400 && res[0].error) {
              text = res[0].error;
          } else {
              text = "Ha ocurrido un al procesar la respuesta, por favor contactar a soporte";
          }
          Swal.fire({
              title: 'Error',
              text: text,
              icon: 'error',
              confirmButtonColor: '#3085d6',
              confirmButtonText: 'Ok',
          })
      }).always(function () {
          removeFileButton.style.cssText = "display: block;";
          uploadButton.innerHTML = `<i class="fa-solid fa-cloud-arrow-up"></i>`;
      })
  } else {
      cannotUploadMessage.style.cssText = "display: flex; animation: fadeIn linear 1.5s;";
  }
});





// $('#downloadExcel').click(function() {
//     // Redireccionar al archivo PDF en Django
//     window.location.href = 'api/descargar-archivo/archivo_nombre';
// })


const generarDatos = () => {

    let infodateexport = [
        ["CEDULA", "NOMBRE EMPLEADO EX-EMPLEADO"],
    ]


        infodateexport.push([
            "00000000000",
            "Nombre Completo",

        ])                
    return infodateexport;
}

const generarExcel = () => {

    /* Crear el archivo Excel */
    var wb = XLSX.utils.book_new();
    var ws = XLSX.utils.aoa_to_sheet(generarDatos());
    XLSX.utils.book_append_sheet(wb, ws, `Entregas por Elemento`);
    
    /* Descargar el archivo Excel */
    var nombreArchivo = `Entregasde${deliveriesNameElement}.xlsx`;
    XLSX.writeFile(wb, nombreArchivo);

}
  
