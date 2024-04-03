
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

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('add-row').addEventListener('click', function () {
        var table = document.getElementById('bill-items-table').getElementsByTagName('tbody')[0];
        var newRow = table.insertRow(table.rows.length);
        var srnoCell = newRow.insertCell(0); 
        var cell1 = newRow.insertCell(1);
        var cell2 = newRow.insertCell(2);
        var cell3 = newRow.insertCell(3);
        var cell4 = newRow.insertCell(4);
        var cell5 = newRow.insertCell(5);
        var cell6 = newRow.insertCell(6);
        var cell7 = newRow.insertCell(7); 
        var cell8 = newRow.insertCell(8); 

        // Update serial number in each row
        for (var i = 0; i < table.rows.length; i++) {
            table.rows[i].cells[0].innerHTML = i + 1;
        }

        cell1.innerHTML = '<input type="text" name="barcode[]" class="form-control" oninput="fetchDispatchData(this)" />';
        cell2.innerHTML = '<input type="text" name="item[]" disabled class="form-control" />';
        cell3.innerHTML = '<input type="number" name="qty[]" oninput="calculateTotal()"  step="1" class="form-control" />';
        cell4.innerHTML = '<input type="text" name="code[]" class="form-control-plaintext" disabled/>'
        cell5.innerHTML = '<input type="number" name="rate[]" oninput="calculateTotal()" step="1" class="form-control" />';
        cell6.innerHTML = '<input type="text" name="total[]" disabled readonly class="form-control" />';
        cell7.innerHTML = '<input type="checkbox" name="noExhangeRefund[]" class="form-check-input" onclick="checkSecondCheckbox(this)"/>';
        cell8.innerHTML = '<button type="button" class="btn btn-danger" onclick="deleteRow(this.parentNode.parentNode)">x</button>';
    });
});

function updateExchangeRefund(sourceCheckbox) {
    var secondCheckbox = document.getElementById("noExchangeRefund");
    console.log(document.getElementById("noExchangeRefund"))
    if (sourceCheckbox && sourceCheckbox.checked) {
        secondCheckbox.checked = true;
    } else {
        secondCheckbox.checked = false;
    }
}

function checkSecondCheckbox(checkbox) {
    var secondCheckbox = document.getElementById('noExchangeRefund');
    secondCheckbox.checked = checkbox.checked;
}

// Function to delete the row
function deleteRow(row) {
    var index = row.rowIndex;
    var table = document.getElementById('bill-items-table').getElementsByTagName('tbody')[0];

    // Check if the index is within the valid range
    if (index > 0 && index <= table.rows.length) {
        table.deleteRow(index - 1); // Adjust the index to be 0-based

        // Update serial number in each row after deletion
        for (var i = 0; i < table.rows.length; i++) {
            table.rows[i].cells[0].innerHTML = i + 1;
        }
    }
}

var grand_total = 0
// Add this part for AJAX post request
$('#form_submit').on('click', function (e) {
    e.preventDefault();

    // Manually create an array to hold form data
    var formData = [];

    // Add data from the additional section
    var cardInputValue = $('#cardInput').val();
    var cashInputValue = $('#cashInput').val();
    var pointsInputValue = $('#pointsInput').val();
    var noExchangeRefundValue = $('#noExchangeRefund').prop('checked') ? 'on' : 'off';

    formData.push({ name: 'cardInput', value: cardInputValue });
    formData.push({ name: 'cashInput', value: cashInputValue });
    formData.push({ name: 'pointsInput', value: pointsInputValue });
    formData.push({ name: 'noExchangeRefund', value: noExchangeRefundValue });
    formData.push({ name: 'grand_total', value: grand_total })

    // Add radio button values
    var discountValue = $('input[name="discount"]:checked').val();
    formData.push({ name: 'discount', value: discountValue });
    formData.push({ name: 'balance', value: (grand_total - cardInputValue - cashInputValue - pointsInputValue) })
    var c = getCookie('csrftoken');
    formData.push({ name: 'csrfmiddlewaretoken', value: c })
    formData.push({ name: 'store_id', value: sessionStorage.getItem('store_id') ?? '' })

    // Manually add items without label
    $('table tr').each(function (index) {
        var barcodeValue = $(this).find('input[name^="barcode"]').val();
        var itemValue = $(this).find('input[name^="item"]').val();
        var qtyValue = $(this).find('input[name^="qty"]').val();
        var rateValue = $(this).find('input[name^="rate"]').val();
        var totalValue = $(this).find('input[name^="total"]').val();

        formData.push({ name: 'barcode[]', value: barcodeValue });
        formData.push({ name: 'item[]', value: itemValue });
        formData.push({ name: 'qty[]', value: qtyValue });
        formData.push({ name: 'rate[]', value: rateValue });
        formData.push({ name: 'total[]', value: totalValue });
    });

    // Manually add other fields as needed

    // Make the AJAX request
    console.log('working')
    $.ajax({
        type: 'POST',
        url: '/pos/save_bill/',
        data: formData,
        success: function (response) {
            alert('saved sucessfully')
            window.location.href = '/pos/bill_print/' + response.sale_no;
        },
        error: function (error) {
            console.log(error);
            // Handle the error as needed
        }
    });
});


// fetch data from barcode:

function fetchDispatchData(barcodeInput) {
    var barcodeValue = barcodeInput.value.trim();
    if (barcodeValue === "") {
        // Clear other fields if barcode is empty
        clearFields(barcodeInput.closest("tr"));
        return;
    }
    // Make an AJAX request to fetch data based on the barcode
    $.ajax({
        type: "GET",
        url: "/pos/fetch_dispatch_data/",
        data: { barcode: barcodeValue },
        dataType: "json",
        success: function (data) {
            console.log("Data received:", data);
            // Update other fields with the fetched data
            var row = barcodeInput.closest("tr");
            updateFields(row, data);
            
            // Update code[] and rate[] fields
            var codeInput = row.querySelector('[name="code[]"]');
            var rateInput = row.querySelector('[name="rate[]"]');

            if (data.Code !== undefined) {
                if (data.Rate !== undefined) {
                    var combinedValue = data.Code + ' - ' + data.Rate;
                    codeInput.value = combinedValue;
                    rateInput.value = data.Rate;
                } else {
                    console.error("Rate is undefined in the API response.");
                }
            } else {
                console.error("Code is undefined in the API response.");
            }
            calculateTotal();

        },
        error: function () {
            console.error("Error fetching data for barcode: " + barcodeValue);
            barcodeInput.closest("tr").querySelector('[name="qty[]"]').value = 1;
            barcodeInput.closest("tr").querySelector('[name="rate[]"]').value = 1;
            calculateTotal();
        }
    });
}



function clearFields(row) {
    // Clear other fields when barcode is empty
    row.querySelector('[name="item[]"]').value = "";
    row.querySelector('[name="qty[]"]').value = "";
    row.querySelector('[name="rate[]"]').value = "";
    row.querySelector('[name="total[]"]').value = "";
}

function updateFields(row, data) {
    // Update other fields with the fetched data
    row.querySelector('[name="item[]"]').value = typeof data.Headline !== 'undefined' ? data.Headline : '';
    row.querySelector('[name="qty[]"]').value = 1
    row.querySelector('[name="code[]"]').value = typeof data.Code !== 'undefined' ? data.Code : '';
    row.querySelector('[name="rate[]"]').value = 0;
    row.querySelector('[name="total[]"]').value = (row.querySelector('[name="qty[]"]').value * data.Rate).toFixed(2);
    calculateTotal()
}

// Add this script to your existing JavaScript file or create a new one

$('.payment-input').hide();
function paymentToggle(value, field) {
    if ($(field).attr('trigger') == 0) {
        $(`#${value}`).show();
        var cardValue = $('#cardInput').val() !== '' ? $('#cardInput').val() : 0;
        var cashValue = $('#cashInput').val() !== '' ? $('#cashInput').val() : 0;
        var pointsValue = $('#pointsInput').val() !== '' ? $('#pointsInput').val() : 0;
        $(`#${value}`).val(grand_total - cardValue - cashValue - pointsValue);
        $(field).css('background-color', '#5AB8AB');
        $(field).attr('trigger', 1);
        calculateTotal();
    } else {
        $(field).attr('trigger', 0);
        $(`#${value}`).hide();
        $(`#${value}`).val('');
        $(field).css('background-color', '#f1f1f1');
        calculateTotal();
    }
}

// add item withouth label

$('#itemInput').on('change', function () {
    addItemToTable();
});

$('#addItemBtn').on('click', function () {
    addItemToTable();
});

function addItemToTable() {
    // Get the selected item from the input
    var selectedItem = $('#itemInput').val();

    // Find the corresponding option in the datalist
    var selectedOption = $('#itemList option[value="' + selectedItem + '"]');

    // If an option is found, extract its attributes
    if (selectedOption.length > 0) {
        var barcode = selectedOption.data('code');
        var item = selectedOption.data('item');
        var qty = selectedOption.data('qty');
        var rate = selectedOption.data('rate');

        // Get the current number of rows
        var rowCount = $('#bill-items-table tbody tr').length;

        // Increment Serial Number
        var srNo = rowCount + 1;

        // Create a new row
        var newRow = '<tr class="item-row">' +
            '<td class="srno">' + srNo + '</td>' +
            '<td><input type="text" name="barcode[]" class="form-control" value="' + barcode + '" oninput="fetchDispatchData(this)" disabled /></td>' +
            '<td><input type="text" name="item[]" class="form-control" value="' + item + '" disabled /></td>' +
            '<td><input type="number" name="qty[]" step="1" class="form-control" oninput="calculateTotal()" value="' + qty + '"  /></td>' +
            '<td><input type="text" name="code[]" class="form-control-plaintext" disabled /></td>' +
            '<td><input type="number" name="rate[]" step="1" class="form-control" oninput="calculateTotal()" value="' + rate + '" /></td>' +
            '<td><input type="text" name="total[]" disabled class="form-control" /></td>' +
            '<td><input type="checkbox" name="noExhangeRefund[]" class="form-check-input" onclick="checkSecondCheckbox(this)" /></td>' +
            '<td><button type="button" class="btn btn-danger btn-remove-row">x</button></td>' +
            '</tr>';

        // Append the new row to the table
        $('#bill-items-table tbody').append(newRow);

        // Event listener for row removal
        $('.btn-remove-row').on('click', function () {
            $(this).closest('tr').remove();
            updateSerialNumbers();
        });

        // Update Serial Numbers
        updateSerialNumbers();
        calculateTotal();

        // Clear the input after adding the item
        $('#itemInput').val('');
    }
}

// Additional JavaScript to make the input searchable (optional)



function updateSerialNumbers() {
    $('#bill-items-table tbody tr').each(function (index) {
        $(this).find('.srno').text(index + 1);
    });
}

$('.fixed-footer button').on('click', function () {
    addItemToTable(this);
});

function calculateTotal() {
    grand_total = 0;
    $('#cardInput').val(parseFloat($('#cardInput').val()).toFixed(2));
    $('#cashInput').val(parseFloat($('#cashInput').val()).toFixed(2));
    $('#pointsInput').val(parseFloat($('#pointsInput').val()).toFixed(2));
    $('#bill-items-table tbody tr').each(function () {
        var qtyInput = $(this).find('input[name="qty[]"]');
        var rateInput = $(this).find('input[name="rate[]"]');
        if (qtyInput.val() !== '') {
            var qty = parseFloat(qtyInput.val());
            var rate = parseFloat(rateInput.val());
            $(this).find('input[name="total[]"]').val(qty * rate)
            var discount = parseFloat(document.querySelector('input[name="discount"]:checked').value); // Parse the discount value
            grand_total += (qty * rate - (qty * rate * discount))
        }
    });

    var cardValue = $('#cardInput').val() !== '' ? parseFloat($('#cardInput').val()) : 0;
    var cashValue = $('#cashInput').val() !== '' ? parseFloat($('#cashInput').val()) : 0;
    var pointsValue = $('#pointsInput').val() !== '' ? parseFloat($('#pointsInput').val()) : 0;

    if (cardValue > 0 || cashValue > 0 || pointsValue > 0) {
        $('#form_submit').prop('disabled', false);
        $('#paymentWarning').text('');
    } else {
        $('#form_submit').prop('disabled', true);
        $('#paymentWarning').text('Please select a payment method.');
    }

    grand_total = Math.ceil(grand_total); 
    $('#grand_total').text('£' + grand_total.toFixed(1));
    var balance = (grand_total - cardValue - cashValue - pointsValue).toFixed(1);
    $('#balance').text('£ ' + balance).css('font-size', 'x-large').css('color', balance < 0 ? 'red' : 'black');
}


// customs buttons
document.addEventListener("DOMContentLoaded", function () {
    var calculatorInput;

    // Add mousedown event listener to the document
    document.addEventListener("mousedown", function (event) {
        var target = event.target;

        if (
            (target.tagName === "INPUT" && target.type === "text") ||
            (target.tagName === "INPUT" && target.type === "number")
        ) {
            // Save the reference to the input field for later use
            calculatorInput = target;
        }
    });

    // Add click event listener to the calculator buttons container
    document.getElementById("calculatorButtons").addEventListener("click", function (event) {
        var button = event.target;

        // Check if the clicked element is a button
        if (button.tagName === "BUTTON") {
            var buttonText = button.textContent;

            // Check if the input field is focused
            var isInputFocused = document.activeElement === calculatorInput;

            // Handle numeric buttons and decimal point
            if (!isNaN(buttonText) || buttonText === ".") {
                calculatorInput.value += buttonText;
            } else if (buttonText === "x") {
                // Handle delete (clear) button
                calculatorInput.value = "";
            }

            // If the input field was focused, set the focus back after button click
            if (isInputFocused) {
                calculatorInput.focus();
            }
        }
    });
});

// function calculateTotalQuantityBySupplier(supplierName) {
//     var totalQuantity = 0;

//     // Loop through the salesData array
//     for (var i = 0; i < salesData.length; i++) {
//         // Check if the supplier name matches
//         if (salesData[i].supplier === supplierName) {
//             // Add the quantity to the total
//             totalQuantity += salesData[i].Qty;
//         }
//     }

//     return totalQuantity;
// }


