$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-articulo").modal("show");
        },
        success: function (data) {
          $("#modal-articulo .modal-content").html(data.html_form);
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
            $("#articulo-table tbody").html(data.html_articulo_list);
            $("#modal-articulo").modal('hide');
          }
          else {
            $("#modal-articulo .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
  
  
    /* Binding */
  
    // Create articulo
    $(".js-create-articulo").click(loadForm);
    $("#modal-articulo").on("submit", ".js-articulo-create-form", saveForm);
  
    // Update articulo
    $("#articulo-table").on("click", ".js-update-articulo", loadForm);
    $("#modal-articulo").on("submit", ".js-articulo-update-form", saveForm);
  
  // Delete articulo
  $("#articulo-table").on("click", ".js-delete-articulo", loadForm);
  $("#modal-articulo").on("submit", ".js-articulo-delete-form", saveForm);
  });