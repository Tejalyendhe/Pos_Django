function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
  $.ajaxSetup({
    headers: { "X-CSRFToken": getCookie("csrftoken") }
  
  });
  
  
var table1
$(document).ready(function () {
    // Function to load table data via AJAX
    $('#download-excel-button').prop("disabled", true);
    function loadInvTableData() {
      // Show the loader
      $('#table-loader').show();
      $.ajax({
        type: 'POST',
        url: '/pos/loadinvoice_table_data/',  // Replace with the correct URL
        dataType: 'json',
        headers: {
          'X-CSRFToken': getCookie('csrftoken')
        },
        success: function (data) {
          // Populate the table with data
          table1 = $('#inv_table').DataTable({
            data: data.table_data,  // Assuming 'table_data' is a list of objects
            columns: [
              { data: null, title: 'Sr.no', render: function (data, type, row, meta) { return meta.row + 1; } },
              { data: 'Invoice_No', title: 'Invoice no.' },
              
              { data: 'Distpatch_numbers', title: 'Distpatch No' },
              {
                data: 'Created_date',
                title: 'Created Date',
                render: function (data, type, row) {
                  // Format the date as "Y-m-d"
                  return new Date(data).toLocaleDateString('en-US', { year: 'numeric', month: '2-digit', day: '2-digit' });
                }
              },
              { data: 'Total_packed_qty', title: 'Total' },
              {
                data: null, title: '', render: function (data, type, row) {
                  if (row.Total_greturn_qty > 0 || row.Total_inward_qty > 0) {
                    return ''+data.Total_inward_qty+' !';
                  } else {
                    return '';
                  }
                }
              },
              {
                data: null, title: '', render: function (data, type, row) {
                  if (row.Total_greturn_qty > 0 || row.Total_inward_qty > 0) {
                    return '<button type="button" class="btn btn-warning mark-as-done-button" onclick="event.stopPropagation(); markAsDoneInv(this.closest(\'tr\'))"><i class="bi bi-check-square"></i></button>';

                  } else {
                    return '';
                  }
                }
              }
            ],
           
            
            searching: true,
            paging: true,
            pageLength: 50,
            createdRow: function (row, data, dataIndex) {
              // Add 'table-warning' class to rows based on your condition
              if (data.Total_greturn_qty > 0 || data.Total_inward_qty > 0) {
                $(row).addClass('table-warning');
              }
              // Add 'clickable-row' class and 'data-href' attribute
              $(row).addClass('data-row');
              $(row).attr('data-href', '/pos/view_product/' + data.Invoice_No + '/');
            }
          });

          // Hide the loader and show the table
          $('#table-loader').hide();
          // $('#inw_table').show();
          $('.data-row').click(function () {
            window.location.href = $(this).data('href');
          });
          // Add a click event handler to the "Mark as Done" buttons
          $('#download-excel-button').removeAttr('disabled');
        },
        error: function () {
          // Handle errors if needed
        }
      });
    }

    // Call the function to load table data
    loadInvTableData();
  });

  function markAsDoneInv(row){
    var formData = new FormData();       
    var c = getCookie('csrftoken');
    formData.append('csrfmiddlewaretoken', c)
    formData.append('inv_no',row.querySelector('td:nth-child(2)').textContent)
    $.ajax({
            type: 'POST',
            url:  '/pos/mark_as_done_inv/',
            dataType: 'json',
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            enctype: 'multipart/form-data',
            success:function (json) {
              if (json.resp === 200) {
                // Remove warning class
                alert('Qty has been moved successfully.')
                $(row).removeClass('table-warning');
                
                // Remove "!" mark
                row.querySelector('td:nth-child(6)').textContent = '';
                
                // Remove the button
                row.querySelector('td:nth-child(7)').innerHTML = '';
              }
              else{
                alert('It seems some error has occured.')
              }
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ":" + xhr.responseText)
                alert(errmsg)
            }
        })
      
  }

    /// Function to download Excel
  
    function decodeEntities(encodedString) {
      var textarea = document.createElement("textarea");
      textarea.innerHTML = encodedString;
      return textarea.value;
  }
document.getElementById("download-excel-button").addEventListener("click", function () {
  // Get the current filtered data from the DataTable
  var filteredData = table1.rows({ search: "applied" }).data().toArray();

  // Convert the filtered data to a new DataFrame
  var filteredDF = new dfd.DataFrame(filteredData, {
      columns: ['Sr.no', 'Invoice No','Distpatch No','Created Date','Total',''],
  });

  // Replace HTML entities in the 'Label Range' column
  

  // Create a new Excel workbook and worksheet
  var workbook = new ExcelJS.Workbook();
  var worksheet = workbook.addWorksheet("Filtered Data");

  // Convert the DataFrame to a worksheet
  var columns = filteredDF.columns;
  worksheet.columns = columns.map((col) => ({ header: col }));

  // Get the data as a 2D array
  var dataValues = filteredDF.values;

  // Add the data to the worksheet
  dataValues.forEach((row) => {
      worksheet.addRow(row);
  });

  var fileName = "invoice_report.xlsx";

  // Generate the Excel file and trigger the download with the dynamic file name
  workbook.xlsx.writeBuffer().then(function (data) {
      var blob = new Blob([data], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
      var url = window.URL.createObjectURL(blob);
      var a = document.createElement("a");
      a.href = url;
      a.download = fileName;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
  });
});

