const form = document.querySelector("form"),
usersField = form.querySelector(".users-field"),
usersInput = usersField.querySelector(".users"),
emailField = form.querySelector(".email-field"),
emailInput = emailField.querySelector(".email"),
passField = form.querySelector(".create-password"),
passInput = passField.querySelector(".password"),
cPassField = form.querySelector(".confirm-password"),
cPassInput = cPassField.querySelector(".cPassword");

function checkEmail() {
    if (true) 
{
    emailField.classList.remove("invalid");
    emailField.classList.remove("invalid2");
    emailField.classList.remove("invalid3");
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,100}$/;
    if (emailInput.value === ''){
        emailField.classList.remove("successfully");
        emailField.classList.remove("invalid");
        emailField.classList.remove("invalid2");
        return emailField.classList.add("invalid3"); }
    if (true) 
    {
        if (!emailInput.value.match(emailPattern)){
        emailField.classList.remove("successfully");
        emailField.classList.remove("invalid");
        emailField.classList.remove("invalid3");
        return emailField.classList.add("invalid2");
    }
    if (true) 
    {
        if (
            !emailField.classList.contains("invalid") &&
            !emailField.classList.contains("invalid2") &&
            !emailField.classList.contains("invalid3")
        ) {
            emailField.classList.remove("invalid");
        emailField.classList.remove("invalid2");
        emailField.classList.remove("invalid3");
        return emailField.classList.add("successfully");
        }
    }}}
    
}


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
  const passPatterrn = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Zа-яА-Я0-9!"#$%&')(*+,-./:;<=>?@^_`|]{8,128}$/;

    passField.classList.remove("invalid2");
    passField.classList.remove("invalid3");
    if (passInput.value === ''){
        passField.classList.remove("successfully");
        passField.classList.remove("invalid2");
        return passField.classList.add("invalid3"); }
    if (true) 
    {
        if (!passInput.value.match(passPatterrn)){
        passField.classList.remove("successfully");
        passField.classList.remove("invalid3");
        return passField.classList.add("invalid2");
    }
    
        if (
            !passField.classList.contains("invalid2") &&
            !passField.classList.contains("invalid3")
        ) {
        passField.classList.remove("invalid2");
        passField.classList.remove("invalid3");
        return passField.classList.add("successfully");
        }
    }}
}


function confirmPass(){
    if (true) 
{
    cPassField.classList.remove("invalid2");
    cPassField.classList.remove("invalid3");
    if (cPassInput.value === ''){
        cPassField.classList.remove("successfully");
        cPassField.classList.remove("invalid2");
        return cPassField.classList.add("invalid3"); }
    if (true) 
    {
        function initialon(){
        if (passInput.value !== cPassInput.value){
        cPassField.classList.remove("successfully");
        cPassField.classList.remove("invalid3");
        return cPassField.classList.add("invalid2"); 
    }
        
        if (
            !cPassField.classList.contains("invalid2") &&
            !cPassField.classList.contains("invalid3")
        ) {
        cPassField.classList.remove("invalid2");
        cPassField.classList.remove("invalid3");
        return cPassField.classList.add("successfully");
        }
    }
    initialon();
    }}
}

var initial;
function checkUsers(){
    if (true) 
    {
        usersField.classList.remove("invalid");
        usersField.classList.remove("invalid2");
        usersField.classList.remove("invalid3");
        const usersPattern = /^[a-яА-Яa-zA-Z0-9-_=+)('"!@#№;$%?&*|/,.]{3,16}$/;
        if (usersInput.value === ''){
            usersField.classList.remove("successfully");
            usersField.classList.remove("invalid");
            usersField.classList.remove("invalid2");
            return usersField.classList.add("invalid3"); }
        if (true) 
        {
            if (!usersInput.value.match(usersPattern)){
            usersField.classList.remove("successfully");
            usersField.classList.remove("invalid");
            usersField.classList.remove("invalid3");
            return usersField.classList.add("invalid2");
        }
        if (true) 
        {   
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
        }}}
}
usersInput.addEventListener("keyup", () => {
    checkUsers();
    validation_check();
});
emailInput.addEventListener("keyup", () => {
    checkEmail();
    validation_check();
});
passInput.addEventListener("keyup", () => {
    createPass();
    validation_check();
    if(!cPassInput.value == ''){
        confirmPass();
    } 
});
cPassInput.addEventListener("keyup", () => {
    confirmPass();
    validation_check();
});


function validation_check()
{
    if (
        usersField.classList.contains("successfully") &&
        emailField.classList.contains("successfully") &&
        passField.classList.contains("successfully") &&
        cPassField.classList.contains("successfully")
    ) {
        document.getElementById('button_form').removeAttribute('disabled');
    }
    else{
        document.getElementById('button_form').disabled = 'disabled';
    }
}
validation_check();


// form.addEventListener("submit", (e) => {
//     e.preventDefault();
//     checkEmail();
//     checkUsers();
//     createPass();
//     confirmPass();
//     if (
//         !usersField.classList.contains("invalid") &&
//         !emailField.classList.contains("invalid") &&
//         !passField.classList.contains("invalid") &&
//         !cPassField.classList.contains("invalid") &&

//         usersField.classList.contains("successfully") &&
//         emailField.classList.contains("successfully") &&
//         passField.classList.contains("successfully") &&
//         cPassField.classList.contains("successfully")
//     ) {
//         location.href = form.getAttribute("method");
//     }
// });
//         let switchMode = document.getElementById("switchMode");
//         let mode_style = document.querySelector(".mode_ i")

//         switchMode.onclick = function () {
//             let theme = document.getElementById("theme");

//             if (theme.getAttribute("href") == "light-mode.css") {
//                 theme.href = "dark-mode.css";
//                 mode_style.classList.remove("bx-sun")
//                 mode_style.classList.add("bx-moon")
//             } else {
//                 theme.href = "light-mode.css"
//                 mode_style.classList.remove("bx-moon")
//                 mode_style.classList.add("bx-sun")
//             }
//         }

//         const filetext = document.querySelector(".upload_text_");
//         const fileinput = document.querySelector(".upload_text");
//         const fileinputContainer = document.querySelector(".upload_input_container");
        
        
//         function getoutput()
//         {
//             const fullPath = document.getElementById('upload').value;  
//     const startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
//     console.log(startIndex);
//     const filename = fullPath.substring(startIndex);
//     console.log(filename);
//     if(filename != ""){
//         filetext.innerHTML = filename;
//         const icon_file = document.querySelector('.bxl-dropbox');
//         icon_file.classList.remove("bx-tada");
//         icon_file.classList.add("bx-package");
//         return true;
//     }
//     icon_file.classList.remove("bx-package");
//         icon_file.classList.add("bx-tada");
//     filetext.innerHTML = "Загрузите файл";
//         }

//         const seconds = document.querySelector(".seconds .number");
//             const minutes = document.querySelector(".minutes .number");
//             const hours = document.querySelector(".hours .number");

//             let secValue = 58,
//             minValue = 30,
//             hourValue = 1

//             const timeFunctin = setInterval(() => {
//                 secValue--;

//                 if (secValue == 0) {
//                     minValue--;
//                     secValue = 60;
//                 }
//                 if (minValue == 0) {
//                     hourValue--;
//                     minValue = 60;
//                 }
//                 seconds.textContent = secValue < 10 ? `0${secValue}` : secValue;
//                 minutes.textContent = minValue < 10 ? `0${minValue}` : minValue;
//                 hours.textContent = hourValue < 10 ? `0${hourValue}` : hourValue;
//             }, 1000);
//             const optionMenu = document.querySelector(".select-menu"),
//             selectBtn = optionMenu.querySelector(".select-btn"),
//             options = optionMenu.querySelectorAll(".option"),
//             sBtn_text = optionMenu.querySelector(".sBtn-text");
          
//      const toggleMenu = function () {
//         optionMenu.classList.toggle("active");
// }

// selectBtn.addEventListener("click", function (e) {
//     e.stopPropagation();
//     toggleMenu();
// });

// document.addEventListener("click", function (e) {
//     const target = e.target;
//     const its_menu = target == optionMenu || optionMenu.contains(target);
//     const its_btnMenu = target == selectBtn;
//     const menu_is_active = optionMenu.classList.contains("active");

//     if (!its_menu && !its_btnMenu && menu_is_active) {
//         toggleMenu();
//     }
// });
//      options.forEach(option =>{
//          option.addEventListener("click", ()=>{
//              let selectedOption = option.querySelector(".option-text").innerText;
//              sBtn_text.innerText = selectedOption;
//              let selectedOptionAttribyteQuerySelector = option.querySelector(".option-text");
//              let selectedOptionAttribyte = selectedOptionAttribyteQuerySelector.dataset.type;
//              fileinput.setAttribute("accept", selectedOptionAttribyte);

     
//              optionMenu.classList.remove("active");
//          });
//      });


//      fileinputContainer.addEventListener("mouseover", ()=> {
//         const icon_file = document.querySelector('.bxl-dropbox');
//         console.log(icon_file);
//         icon_file.classList.add("bx-tada");
//      });
//      fileinputContainer.addEventListener("mouseout", ()=> {
//         const icon_file = document.querySelector('.bxl-dropbox');
//         console.log(icon_file)
//         icon_file.classList.remove("bx-tada")
//      });

//      const tabs = document.querySelectorAll(".tab");
// const contents = document.querySelectorAll(".content");
 
// for (let i = 0; i < tabs.length; i++) {
// 	tabs[i].addEventListener("click", ( event ) => {
 
// 		let tabsChildren = event.target.parentElement.children;
// 		for (let t = 0; t < tabsChildren.length; t++) {
// 			tabsChildren[t].classList.remove("tab--active");
// 		}
// 		tabs[i].classList.add("tab--active");
// 		let tabContentChildren = document.querySelector('.container_content').children;
// 		for (let c = 0; c < tabContentChildren.length; c++) {
// 			tabContentChildren[c].classList.remove("content--active");
// 		}
// 		contents[i].classList.add("content--active");
 
// 	});
// }//         let switchMode = document.getElementById("switchMode");
//         let mode_style = document.querySelector(".mode_ i")

//         switchMode.onclick = function () {
//             let theme = document.getElementById("theme");

//             if (theme.getAttribute("href") == "light-mode.css") {
//                 theme.href = "dark-mode.css";
//                 mode_style.classList.remove("bx-sun")
//                 mode_style.classList.add("bx-moon")
//             } else {
//                 theme.href = "light-mode.css"
//                 mode_style.classList.remove("bx-moon")
//                 mode_style.classList.add("bx-sun")
//             }
//         }

//         const filetext = document.querySelector(".upload_text_");
//         const fileinput = document.querySelector(".upload_text");
//         const fileinputContainer = document.querySelector(".upload_input_container");
        
        
//         function getoutput()
//         {
//             const fullPath = document.getElementById('upload').value;  
//     const startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
//     console.log(startIndex);
//     const filename = fullPath.substring(startIndex);
//     console.log(filename);
//     if(filename != ""){
//         filetext.innerHTML = filename;
//         const icon_file = document.querySelector('.bxl-dropbox');
//         icon_file.classList.remove("bx-tada");
//         icon_file.classList.add("bx-package");
//         return true;
//     }
//     icon_file.classList.remove("bx-package");
//         icon_file.classList.add("bx-tada");
//     filetext.innerHTML = "Загрузите файл";
//         }

//         const seconds = document.querySelector(".seconds .number");
//             const minutes = document.querySelector(".minutes .number");
//             const hours = document.querySelector(".hours .number");

//             let secValue = 58,
//             minValue = 30,
//             hourValue = 1

//             const timeFunctin = setInterval(() => {
//                 secValue--;

//                 if (secValue == 0) {
//                     minValue--;
//                     secValue = 60;
//                 }
//                 if (minValue == 0) {
//                     hourValue--;
//                     minValue = 60;
//                 }
//                 seconds.textContent = secValue < 10 ? `0${secValue}` : secValue;
//                 minutes.textContent = minValue < 10 ? `0${minValue}` : minValue;
//                 hours.textContent = hourValue < 10 ? `0${hourValue}` : hourValue;
//             }, 1000);
//             const optionMenu = document.querySelector(".select-menu"),
//             selectBtn = optionMenu.querySelector(".select-btn"),
//             options = optionMenu.querySelectorAll(".option"),
//             sBtn_text = optionMenu.querySelector(".sBtn-text");
          
//      const toggleMenu = function () {
//         optionMenu.classList.toggle("active");
// }

// selectBtn.addEventListener("click", function (e) {
//     e.stopPropagation();
//     toggleMenu();
// });

// document.addEventListener("click", function (e) {
//     const target = e.target;
//     const its_menu = target == optionMenu || optionMenu.contains(target);
//     const its_btnMenu = target == selectBtn;
//     const menu_is_active = optionMenu.classList.contains("active");

//     if (!its_menu && !its_btnMenu && menu_is_active) {
//         toggleMenu();
//     }
// });
//      options.forEach(option =>{
//          option.addEventListener("click", ()=>{
//              let selectedOption = option.querySelector(".option-text").innerText;
//              sBtn_text.innerText = selectedOption;
//              let selectedOptionAttribyteQuerySelector = option.querySelector(".option-text");
//              let selectedOptionAttribyte = selectedOptionAttribyteQuerySelector.dataset.type;
//              fileinput.setAttribute("accept", selectedOptionAttribyte);

     
//              optionMenu.classList.remove("active");
//          });
//      });


//      fileinputContainer.addEventListener("mouseover", ()=> {
//         const icon_file = document.querySelector('.bxl-dropbox');
//         console.log(icon_file);
//         icon_file.classList.add("bx-tada");
//      });
//      fileinputContainer.addEventListener("mouseout", ()=> {
//         const icon_file = document.querySelector('.bxl-dropbox');
//         console.log(icon_file)
//         icon_file.classList.remove("bx-tada")
//      });

//      const tabs = document.querySelectorAll(".tab");
// const contents = document.querySelectorAll(".content");
 
// for (let i = 0; i < tabs.length; i++) {
// 	tabs[i].addEventListener("click", ( event ) => {
 
// 		let tabsChildren = event.target.parentElement.children;
// 		for (let t = 0; t < tabsChildren.length; t++) {
// 			tabsChildren[t].classList.remove("tab--active");
// 		}
// 		tabs[i].classList.add("tab--active");
// 		let tabContentChildren = document.querySelector('.container_content').children;
// 		for (let c = 0; c < tabContentChildren.length; c++) {
// 			tabContentChildren[c].classList.remove("content--active");
// 		}
// 		contents[i].classList.add("content--active");
 
// 	});
// }