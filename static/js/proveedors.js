$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-proveedor").modal("show");
        },
        success: function (data) {
          $("#modal-proveedor .modal-content").html(data.html_form);
        }
      });
    };
  
    var saveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#proveedor-table tbody").html(data.html_proveedor_list);
            $("#modal-proveedor").modal('hide');
          }
          else {
            $("#modal-proveedor .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
  
  
    /* Binding */
  
    // Create book
    $(".js-create-proveedor").click(loadForm);
    $("#modal-proveedor").on("submit", ".js-proveedor-create-form", saveForm);
  
    // Update book
    $("#proveedor-table").on("click", ".js-update-proveedor", loadForm);
    $("#modal-proveedor").on("submit", ".js-proveedor-update-form", saveForm);
  
  // Delete book
  $("#proveedor-table").on("click", ".js-delete-proveedor", loadForm);
  $("#modal-proveedor").on("submit", ".js-proveedor-delete-form", saveForm);
  });