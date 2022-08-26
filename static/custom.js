$("tr").removeAttr("style");
$("thead").addClass("thead-dark");
var table = $("table").DataTable({
    processing: true,
    'language': {
    'loadingRecords': '&nbsp;',
    'processing': '<div class="spinner"></div>'
} ,
    "pagingType": "full_numbers",
"paging": true,
"lengthMenu": [10, 25, 50, 75, 100],
    dom: 'Blfrtip',
    buttons: [
        {
            text: 'Add new record',
            className: 'btn btn-info btn-sm mb-2 mt-2',
            action: function (e, dt, node, config) {
                window.location = '/addrecord';
            }
        },
        {
            text: 'Download CSV',
            className: 'btn btn-info btn-sm mb-2 mt-2 download-btn',
            action: function (e, dt, node, config) {
                window.location = '/download_file';
            }
        },
        {
            text: 'Delete Record',
            className: 'del_record btn btn-danger btn-sm mb-2 mt-2',
            action: function (e, dt, node, config) {
                table.row('.selected').remove().draw(false);
            }
        }
    ],
    select: true,

});

$("tr").click(function(){
    selected_row= table.row( this ).data()
    selected_row= JSON.stringify(selected_row)
        $(".del_record").click(function(){
        console.log(selected_row);
            $.ajax({
            url: '/delete_record',
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: "json",
            data: selected_row,
            success: function(result) {
                console.log('deleted sucessfully', selected_row)
                }
            });
        });
});
