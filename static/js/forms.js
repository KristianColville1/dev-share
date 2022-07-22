$(document).ready(()=> {

    /* Login Form */
    let username_box = $('#id_login').parent();
    let password_box = $('#id_password').parent();

    $('#id_login').addClass('rounded-pill text-center input-field');
    $('#id_password').addClass('rounded-pill text-center input-field');

    $(username_box).addClass('input-icons');
    $(username_box).prepend('<i class="fa-solid fa-envelope position-absolute input-icons mx-3"></i>');
    $(password_box).addClass('input-icons');
    $(password_box).prepend('<i class="fa-solid fa-user position-absolute input-icons mx-3"></i>');
    /* end of Login Form */

});