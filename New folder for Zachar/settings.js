const eyeIcons = document.querySelectorAll(".show-hide");

eyeIcons.forEach((eyeIcon) => {
    eyeIcon.addEventListener("click", () => {
        const pInput = eyeIcon.parentElement.querySelector("input");
        
        if(pInput.type === "password"){
            eyeIcon.classList.replace("bx-hide", "bx-show");
            return pInput.type = "text";
        }
        eyeIcon.classList.replace("bx-show", "bx-hide");
        return pInput.type = "password";
    });
});

const change_settings_1 = document.querySelector(".a_1"),
    change_settings_2 = document.querySelector(".a_2"),
    display_set = document.querySelectorAll(".d-settings"),
    list_w1 = document.querySelector(".w_1"),
    bxrightarrowalt = document.querySelector(".bx-right-arrow-alt1"),
    bxrightarrowalt2 = document.querySelector(".bx-right-arrow-alt2"),
    oppacty2 = document.getElementById("oppacty2"),
    oppacty1 = document.getElementById("oppacty1"),
    list_w2 = document.querySelector(".w_2");
console.log(change_settings_1)
    change_settings_1.addEventListener("click", () => {
        if (list_w1.classList.contains('active_1')) {
            list_w1.classList.remove("active_1");
            list_w1.classList.add("inactive_1");
        
            bxrightarrowalt.style.transform = 'rotate(0deg)'; 
            oppacty1.style.opacity = '0';
        }
        else {
            list_w1.classList.add("active_1");
            list_w1.classList.remove("inactive_1");
            bxrightarrowalt.style.transform = 'rotate(90deg)';
            oppacty1.style.opacity = '1';
            if (list_w2.classList.contains('active_2')) {
                list_w2.classList.remove("active_2");
                list_w2.classList.add("inactive_2");
                bxrightarrowalt2.style.transform = 'rotate(0deg)';
                oppacty2.style.opacity = '0';
            }
        }
        
    });
    change_settings_2.addEventListener("click", () => {
        if (list_w2.classList.contains('active_2')) {
            list_w2.classList.remove("active_2");
            list_w2.classList.add("inactive_2");
            
            bxrightarrowalt2.style.transform = 'rotate(0deg)'; 
            oppacty2.style.opacity = '0';
        }
            
        else {
            list_w2.classList.add("active_2");
            list_w2.classList.remove("inactive_2");
            bxrightarrowalt2.style.transform = 'rotate(90deg)'; 
            oppacty2.style.opacity = '1';
            if (list_w1.classList.contains('active_1')) {
                list_w1.classList.remove("active_1");
                list_w1.classList.add("inactive_1");
                bxrightarrowalt.style.transform = 'rotate(0deg)'; 
                oppacty1.style.opacity = '0';
            }
        }
    });
    const const_email = document.getElementById("const_email"),
        const_password = document.getElementById("const_password"),
        email_password = document.getElementById("email_password"),
        password_new = document.getElementById("password_new"),
        Cpassword_new = document.getElementById("Cpassword_new"),
        user_name = document.getElementById("user_name"),
        form_nickname = document.getElementById("form_nickname"),
        form_mail = document.getElementById("form_mail"),
        form_mail_password = document.getElementById("form_mail_password"),
        form_password = document.getElementById("form_password"),
        passwordValueNew = document.getElementById("passwordValueNew"),
        passwordValue = document.getElementById("passwordValue"),
        CpasswordValueNew = document.getElementById("CpasswordValueNew")

function checkUsers(){
    if (true) 
    {
        form_nickname.classList.remove("invalid");
        form_nickname.classList.remove("invalid2");
        form_nickname.classList.remove("invalid3");
        const usersPattern = /^[a-zA-Zа-яА-Я0-9!"#$%&')(*+,-./:;<=>?@^_`|]{3,16}$/;
        if (user_name.value === ''){
            form_nickname.classList.remove("successfully");
            form_nickname.classList.remove("invalid");
            form_nickname.classList.remove("invalid2");
            return form_nickname.classList.add("invalid3"); }
        if (true) 
        {
            if (!user_name.value.match(usersPattern)){
            form_nickname.classList.remove("successfully");
            form_nickname.classList.remove("invalid");
            form_nickname.classList.remove("invalid3");
            return form_nickname.classList.add("invalid2");
        }
        if (true) 
        {   
            if (
                !form_nickname.classList.contains("invalid") &&
                !form_nickname.classList.contains("invalid2") &&
                !form_nickname.classList.contains("invalid3")
            ) {
                form_nickname.classList.remove("invalid");
            form_nickname.classList.remove("invalid2");
            form_nickname.classList.remove("invalid3");
            return form_nickname.classList.add("successfully");
            } 
        }}}
};
function checkEmail() {
    if (true) 
{
    form_mail.classList.remove("invalid");
    form_mail.classList.remove("invalid2");
    form_mail.classList.remove("invalid3");
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,100}$/;
    if (const_email.value === ''){
        form_mail.classList.remove("successfully");
        form_mail.classList.remove("invalid");
        form_mail.classList.remove("invalid2");
        return form_mail.classList.add("invalid3"); }
    if (true) 
    {
        if (!const_email.value.match(emailPattern)){
            form_mail.classList.remove("successfully");
            form_mail.classList.remove("invalid");
            form_mail.classList.remove("invalid3");
        return form_mail.classList.add("invalid2");
    }
    if (true) 
    {
        if (
            !form_mail.classList.contains("invalid") &&
            !form_mail.classList.contains("invalid2") &&
            !form_mail.classList.contains("invalid3")
        ) {
            form_mail.classList.remove("invalid");
            form_mail.classList.remove("invalid2");
            form_mail.classList.remove("invalid3");
        return form_mail.classList.add("successfully");
        }
    }}}
    
}
user_name.addEventListener("keyup", () => {
    checkUsers();
    validation_check_form_nickname();
});
function createPass(){
    if (true) 
{
    email_password.classList.remove("invalid2");
    email_password.classList.remove("invalid3");
    if (email_password.value === ''){
        email_password.classList.remove("successfully");
        email_password.classList.remove("invalid2");
        return email_password.classList.add("invalid3"); }
    if (true) 
    {
        if (
            !email_password.classList.contains("invalid2") &&
            !email_password.classList.contains("invalid3")
        ) {
        email_password.classList.remove("invalid2");
        email_password.classList.remove("invalid3");
        return email_password.classList.add("successfully");
        }
    }}
}
const_email.addEventListener("keyup", () => {
    checkEmail();
    validation_check_form_mail();
});
email_password.addEventListener("keyup", () => {
    createPass();
    validation_check_form_mail();
});

function validation_check_form_nickname()
{
    if (
        form_nickname.classList.contains("successfully") 
    ) {
        document.getElementById('user_submit').removeAttribute('disabled');
    }
    else{
        document.getElementById('user_submit').disabled = 'disabled';
    }
}
validation_check_form_nickname();




function validation_check_form_mail()
{
    if (
        const_email.classList.contains("successfully") &&
        email_password.classList.contains("successfully") 
    ) {
        document.getElementById('email_submit').removeAttribute('disabled');
    }
    else{
        document.getElementById('email_submit').disabled = 'disabled';
    }
}
validation_check_form_mail();


function createNewPass(){
    if (true) 
{
  const passPatterrn = 
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8,128}$/;

    passwordValueNew.classList.remove("invalid2");
    passwordValueNew.classList.remove("invalid3");
    if (password_new.value === ''){
        passwordValueNew.classList.remove("successfully");
        passwordValueNew.classList.remove("invalid2");
        return passwordValueNew.classList.add("invalid3"); }
    if (true) 
    {
        if (!password_new.value.match(passPatterrn)){
        passwordValueNew.classList.remove("successfully");
        passwordValueNew.classList.remove("invalid3");
        return passwordValueNew.classList.add("invalid2");
    }
    
        if (
            !passwordValueNew.classList.contains("invalid2") &&
            !passwordValueNew.classList.contains("invalid3")
        ) {
        passwordValueNew.classList.remove("invalid2");
        passwordValueNew.classList.remove("invalid3");
        return passwordValueNew.classList.add("successfully");
        }
    }}
}
password_new.addEventListener("keyup", () => {
    createNewPass();
    confirmPass();
    validation_check_form_password();
});


function confirmPass(){
    if (true) 
{
    CpasswordValueNew.classList.remove("invalid2");
    CpasswordValueNew.classList.remove("invalid3");
    if (Cpassword_new.value === ''){
        CpasswordValueNew.classList.remove("successfully");
        CpasswordValueNew.classList.remove("invalid2");
        return CpasswordValueNew.classList.add("invalid3"); }
    if (true) 
    {
        function initialon(){
        if (password_new.value !== Cpassword_new.value){
            CpasswordValueNew.classList.remove("successfully");
            CpasswordValueNew.classList.remove("invalid3");
        return CpasswordValueNew.classList.add("invalid2"); 
    }
        
        if (
            !CpasswordValueNew.classList.contains("invalid2") &&
            !CpasswordValueNew.classList.contains("invalid3")
        ) {
        CpasswordValueNew.classList.remove("invalid2");
        CpasswordValueNew.classList.remove("invalid3");
        return CpasswordValueNew.classList.add("successfully");
        }
    }
    initialon();
    }}
}
Cpassword_new.addEventListener("keyup", () => {
    confirmPass();
    validation_check_form_password();
});

function validation_check_form_password()
{
    if (
        const_password.classList.contains("successfully") &&
        password_new.classList.contains("successfully") &&
        Cpassword_new.classList.contains("successfully")
    ) {
        document.getElementById('password_submit').removeAttribute('disabled');
    }
    else{
        document.getElementById('password_submit').disabled = 'disabled';
    }
}
validation_check_form_password();





let popupBg = document.querySelector('.popup__bg'); // Фон попап окна
let popup = document.querySelector('.popup'); // Само окно
let openPopupButtons = document.querySelector('.open-popup'); // Кнопки для показа окна
let closePopupButton = document.querySelector('.close-popup'); // Кнопка для скрытия окна

 // Перебираем все кнопки
openPopupButtons.addEventListener('click', (e) => { // Для каждой вешаем обработчик событий на клик
    e.preventDefault(); // Предотвращаем дефолтное поведение браузера
    popupBg.classList.add('active'); // Добавляем класс 'active' для фона
    popup.classList.add('active'); // И для самого окна
});

closePopupButton.addEventListener('click',() => { // Вешаем обработчик на крестик
    popupBg.classList.remove('active'); // Убираем активный класс с фона
    popup.classList.remove('active'); // И с окна
});

document.addEventListener('click', (e) => { // Вешаем обработчик на весь документ
    if(e.target === popupBg) { // Если цель клика - фот, то:
        popupBg.classList.remove('active'); // Убираем активный класс с фона
        popup.classList.remove('active'); // И с окна
    }
});