//function add_new_table(){
//    $('#make_table').append()
//}
var table_count = 0


$(document).ready(function(){
    $("#btn-add-table").click(function(){
        $("#make_table").append('<div class="row" id="' + 'row_' + table_count + '">' +
                    '<div class="col-md-3">' +
                        '<div class="mb-3">' +
                            '<label class="form-label">Chọn kiểu nối</label>' +
                            '<select name="state" class="form-control">' +
                                '<option value="">LEFT JOIN</option>' +
                                '<option value="">INNER JOIN</option>' +
                                '<option value="">RIGHT JOIN</option>' +
                            '</select>' +
                        '</div>' +
                    '</div>' +
                    '<div class="col-md-3">' +
                        '<div class="mb-3">' +
                            '<label class="form-label">Chọn bảng nối</label>' +
                            '<select name="state" class="form-control">' +
                                '<option value="">T24_STMT_ENTRY</option>' +
                                '<option value="">T24_LIMIT</option>' +
                                '<option value="">T24_FUNDTRANSFER</option>' +
                            '</select>' +
                        '</div>' +
                    '</div>' +
                    '<div class="col-md-3">' +
                        '<label style="display: block;">Action</label>' +
                        '<button id="' + 'btn_remove_' + table_count + '" type="button" class="btn btn-outline-danger" onclick="remove_table(' + 'row_' + table_count + ')">' +
                            '<i class="fa-regular fa fa-trash-can"></i> Xóa' +
                        '</button>' +
                    '</div>' +
                '</div>');

        // disable nút trước đó
        if (table_count > 0) {
            $('#btn_remove_' + (table_count-1)).prop("disabled", true);
        }

        // tăng biến đếm
        table_count++;
        console.log('before:' + table_count)
    });
});


function remove_table(id) {
    $(id).remove()
    table_count--
    $('#btn_remove_' + (table_count-1)).prop("disabled", false);
    console.log('after: ' + table_count)
}
