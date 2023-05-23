$(`#add_table_search, #add_table_loading, #trigger_excel`).hide();


let deliveriesBy = []
let deliveriesNameElement = null



$("#btn_delivery").click(function() {
    $(`#add_table_search, #add_table_loading` ).show();
    $(`#search_id_table_wrapper, #search_id_table, #btn_triggerExcel`).remove();
    
    
    $.ajax({
            type: "GET",
            url: `${baseUrl}/api/queries_coincidences/${$('#picker_date_start').val()}/${$('#picker_date_end').val()}`,

        }).done(function (data) {
            deliveriesBy = []
            deliveriesBy.push(data)
            data.length >=1 ? validate = true : validate = false;
            
            const nuevaFila = $(`
            <table id="search_id_table" class="table nowrap responsive table-striped dt-responsive" width="100%">
                <thead>
                    <tr>
                        <th data-priority="1">C.C</th>
                        <th>Nombre</th>
                        <th>Fecha Retiro</th>
                        <th>Observacion</th>
                        <th>Avance</th>
                    </tr>
                </thead>
                <tbody>
                </tbody>
                <tfoot>
                    <tr>
                        <th data-priority="1">C.C</th>
                        <th>Nombre</th>
                        <th>Fecha Retiro</th>
                        <th>Observacion</th>
                        <th>Avance</th>
                    </tr>
                </tfoot>
            </table>

            <div id='btn_triggerExcel' class="d-flex flex-row justify-content-end card-footer mt-3 pt-4">
                <button class="btn btn-primary" type="button" onclick="generarExcel(${validate})">
                <i class="fa-solid fa-file-excel"></i> Generar Excel</button>
            </div>
            `);

            $("#add_table_search #add_table_loading").append(nuevaFila);

            record_listing(data)
        })

});


const record_listing = (data) => {
    
    $('#search_id_table').DataTable({

        responsive: true,
        data: data,

        "columns": [
            { "data": "identification" },
            { "data": "name" },
            { "data": "withdrawal_date" },
            { "data": "observations" },
            { "data": "avance" },
     
        ],
        "pageLength": 5,
        "order": [[0, "desc"]],
    });
    generarDatos()
}






const generarDatos = () => {

    let infodateexport = [
        ["FECHA DE CONSULTA","COINCIDENCIA","CEDULA", "NOMBRE EMPLEADO EX-EMPLEADO", "FECHA DE RETIRO", "OBSERVACIONES", 'AVANCE'],
    ]

    console.log(deliveriesBy);
    deliveriesBy.map(data => {
        
        data.map(elemt => {
            if (elemt.record === 1) {
                let valdate = elemt.consul_date.split('T')
                console.log(valdate);
                infodateexport.push([
                    valdate[0],
                    "TUVO COINCIDENCIA",
                    elemt.identification,
                    elemt.name,
                    elemt.withdrawal_date,
                    elemt.observations,
                    elemt.avance
                ])                
            }else{
                infodateexport.push([
                    valdate[0],
                    "NO TUVO COINCIDENCIA",
                    elemt.identification,
                    elemt.name,
                    elemt.withdrawal_date,
                    elemt.observations,
                    elemt.avance
                ])  
            }

        });    
    });


    return infodateexport;
}

const generarExcel = (validate) => {

    if(validate){
        /* Crear el archivo Excel */
        var wb = XLSX.utils.book_new();
        var ws = XLSX.utils.aoa_to_sheet(generarDatos());
        XLSX.utils.book_append_sheet(wb, ws, `Reporte`);
      
        /* Descargar el archivo Excel */
        var nombreArchivo = `Reporte Consultas & Conincidencias.xlsx`;
        XLSX.writeFile(wb, nombreArchivo);
    }else{
        Swal.fire('¡Advertencia!', 'Al parecer no hay ninguna información con las fechas ingresadas ', 'warning');
    }

}
  