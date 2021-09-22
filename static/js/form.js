$(document).ready(function () {
    $("#requestForm").validate({
        errorClass: "error fail-alert",
        validClass: "valid success-alert",
        rules: {
            name: {
                required: true,
                minlength: 3,
            },
            email: {
                required: true,
                email: true,
                
            },
            booktitle: {
                required: true,
                minlength: 3,
            },
            Author: {
                required: true,
                minlength: 3

            },
            Genre: {
                required: true,
             
            }
        },
        messages: {
            name: {
                minlength: "Name should be at least 3 characters",
            },
            email: {
                required: "Please enter your email",
                email: "The email should be in the format: abc@domain.tld",

            },
            booktitle: {
                required: "This Feild is Required",
            },
            Author: {
                required: "This Feild is Required"
            },
            Genre:{
                required:"This Feild is Required"
            }
        },
    });


});