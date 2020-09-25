$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-meta").modal("show");
      },
      success: function (data) {
        $("#modal-meta .modal-content").html(data.html_form);
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
          $("#meta-table tbody").html(data.html_meta_list);
          $("#modal-meta").modal('hide');
        }
        else {
          $("#modal-meta .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };



  $(".js-create-meta").click(loadForm);
  $("#modal-meta").on("submit", ".js-meta-create-form", saveForm);


  $("#meta-table").on("click", ".js-update-meta", loadForm);
  $("#modal-meta").on("submit", ".js-meta-update-form", saveForm);


$("#meta-table").on("click", ".js-delete-meta", loadForm);
$("#modal-meta").on("submit", ".js-meta-delete-form", saveForm);
});