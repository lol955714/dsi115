$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-asignacion").modal("show");
        },
        success: function (data) {
          $("#modal-asignacion .modal-content").html(data.html_form);
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
            $("#asignacion-table tbody").html(data.html_asignacion_list);
            $("#modal-asignacion").modal('hide');
          }
          else {
            $("#modal-asignacion .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
    
    /* Binding */
  
    // Create 
    $(".js-create-asignacion").click(loadForm);
    $("#modal-asignacion").on("submit", ".js-asignacion-create-form", saveForm);
  
    // Update 
    $("#asignacion-table").on("click", ".js-update-asignacion", loadForm);
    $("#modal-asignacion").on("submit", ".js-asignacion-update-form", saveForm);
  
  // Delete 
  $("#asignacion-table").on("click", ".js-delete-asignacion", loadForm);
  $("#modal-asignacion").on("submit", ".js-asignacion-delete-form", saveForm);
  });