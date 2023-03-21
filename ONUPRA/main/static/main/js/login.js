const form = document.querySelector("form"),
usersField = form.querySelector(".users-field"),
usersInput = usersField.querySelector(".users"),
passField = form.querySelector(".create-password"),
passInput = passField.querySelector(".password")

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


function createPass(){
    if (true) 
{

    passField.classList.remove("invalid2");
    passField.classList.remove("invalid3");
    if (passInput.value === ''){
        passField.classList.remove("successfully");
        passField.classList.remove("invalid2");
        return passField.classList.add("invalid3"); }
    if (
            !passField.classList.contains("invalid2") &&
            !passField.classList.contains("invalid3")
        ) {
        passField.classList.remove("invalid2");
        passField.classList.remove("invalid3");
        return passField.classList.add("successfully");
        }}
}



var initial;
function checkUsers(){
    if (true) 
    {
        usersField.classList.remove("invalid");
        usersField.classList.remove("invalid2");
        usersField.classList.remove("invalid3");
        if (usersInput.value === ''){
            usersField.classList.remove("successfully");
            usersField.classList.remove("invalid");
            usersField.classList.remove("invalid2");
            return usersField.classList.add("invalid3"); }
         
            if (
                !usersField.classList.contains("invalid") &&
                !usersField.classList.contains("invalid2") &&
                !usersField.classList.contains("invalid3")
            ) {
                usersField.classList.remove("invalid");
            usersField.classList.remove("invalid2");
            usersField.classList.remove("invalid3");
            return usersField.classList.add("successfully");
            } 
        }
}
// usersInput.addEventListener("keyup", checkUsers);
// passInput.addEventListener("keyup", createPass);

// form.addEventListener("submit", (e) => {
//     e.preventDefault();
//     checkUsers();
//     createPass();
//     if (
//         !usersField.classList.contains("invalid") &&
//         !passField.classList.contains("invalid")
//     ) {
//         location.href = form.getAttribute("method");
//     }
// });
usersInput.addEventListener("keyup", () => {
    checkUsers();
    validation_check();
});
passInput.addEventListener("keyup", () => {
    createPass();
    validation_check();
});
function validation_check()
{
    if (
        usersField.classList.contains("successfully") &&
        passField.classList.contains("successfully")
    ) {
        document.getElementById('button_form').removeAttribute('disabled');
    }
    else{
        document.getElementById('button_form').disabled = 'disabled';
    }
}
validation_check();