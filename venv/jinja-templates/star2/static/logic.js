function colllectForm() {
    formData = $('#loginForm').serialize()
    console.log(formData)
}

function init() {
    $('#submitLogin').click(colllectForm)
}

// $(document).ready(init)