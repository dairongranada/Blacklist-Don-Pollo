$(document).ready(function () {
    employee_table = $('#employee_table').DataTable({
        responsive: true,
        "language": {
            "url": 'https://cdn.datatables.net/plug-ins/1.11.3/i18n/es_es.json'
        },
        ajax: {
            type: "GET",
            dataType: "json",
            url: `${baseUrl}/api/employees`,
            dataSrc: "",
        },
        "columns": [         
            { "data": "identification" },
            { "data": "name" },
            { "data": "withdrawal_date" },
            { "data": "observations" },
            { "data": "avance" },


     
        ],
        "pageLength": 3,
        "order": [[0, "desc"]],
    });
});
