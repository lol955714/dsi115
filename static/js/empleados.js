$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-empleado").modal("show");
        },
        success: function (data) {
          $("#modal-empleado .modal-content").html(data.html_form);
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
            $("#empleado-table tbody").html(data.html_empleado_list);
            $("#modal-empleado").modal('hide');
          }
          else {
            $("#modal-empleado .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
  
  
    /* Binding */
  
    // Create empleado
    $(".js-create-empleado").click(loadForm);
    $("#modal-empleado").on("submit", ".js-empleado-create-form", saveForm);
  
    // Update empleado
    $("#empleado-table").on("click", ".js-update-empleado", loadForm);
    $("#modal-empleado").on("submit", ".js-empleado-update-form", saveForm);
  
  // Delete empleado
  $("#empleado-table").on("click", ".js-delete-empleado", loadForm);
  $("#modal-empleado").on("submit", ".js-empleado-delete-form", saveForm);
  });