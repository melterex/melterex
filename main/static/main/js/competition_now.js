const filetext = document.querySelector(".upload_text_");
const fileinput = document.querySelector(".upload_text");
const fileinputContainer = document.querySelector(".upload_input_container");
const button_task = document.querySelector(".button-task");
const stn_text = document.querySelector(".sBtn-text");
const select_menu = document.querySelector(".select-menu");
console.log(stn_text)
function blocked_button_task()
{
    if(stn_text.classList.contains("blocked_text")){
        button_task.disabled = 'disabled';
    }
    else{
        button_task.removeAttribute('disabled');

    }
}
blocked_button_task();
        
function getoutput()
    {
const fullPath = document.getElementById('upload').value;  
const startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
const filename = fullPath.substring(startIndex);
const icon_file = document.querySelector('.bxl-dropbox');
    if(filename != ""){
        filetext.innerHTML = filename;
        icon_file.classList.remove("bx-tada");
        icon_file.classList.add("bx-package");
        return true;
    }
    icon_file.classList.remove("bx-package");
        icon_file.classList.add("bx-tada");
    filetext.innerHTML = "Загрузите файл";
        }



if(document.querySelector(".time_settings").textContent === "--:--:--"){
    ;
}
else{
    const seconds = document.querySelector(".seconds .number");
    const minutes = document.querySelector(".minutes .number");
    const hours = document.querySelector(".hours .number");

    let secValue = document.querySelector(".seconds .number").textContent,
    minValue = document.querySelector(".minutes .number").textContent,
    hourValue = document.querySelector(".hours .number").textContent

    const timeFunctin = setInterval(() => {
        if (hourValue != 0 || minValue != 0 || secValue != 0){
            secValue--;
        }
        if(hourValue == 0 && minValue == 0 && secValue == 0){
            location.reload();
        }
        if (secValue == 0) {
            minValue--;
            secValue = 59;
        }
        if (minValue == 0 && hourValue != 0) {
            hourValue--;
            minValue = 59;
        }
        seconds.textContent = secValue < 10 ? `0${secValue}` : secValue;
        minutes.textContent = minValue < 10 ? `${minValue}` : minValue;
        hours.textContent = hourValue < 10 ? `${hourValue}` : hourValue;
    }, 1000);
}

// const timeFunctin = setInterval(() => {
//     const seconds_text = document.querySelector(".seconds .number").textContent;
//     const minutes_text = document.querySelector(".minutes .number").textContent;
//     const hours_text = document.querySelector(".hours .number").textContent;

//     const seconds = document.querySelector(".seconds .number");
//     const minutes = document.querySelector(".minutes .number");
//     const hours = document.querySelector(".hours .number");

//     seconds.textContent = seconds_text < 10 ? '0${seconds_text}' : seconds_text;
//     minutes.textContent = minutes_text < 10 ? '0${minutes_text}' : minutes_text;
//     hours.textContent = hours_text < 10 ? '0${hours_text}' : hours_text;
//     console.log(seconds_text, minutes_text, hours_text, seconds, minutes, hours)
// }, 1000);

const optionMenu = document.querySelector(".select-menu"),
selectBtn = optionMenu.querySelector(".select-btn"),
options = optionMenu.querySelectorAll(".option"),
sBtn_text = optionMenu.querySelector(".sBtn-text");
          
const toggleMenu = function () {
    optionMenu.classList.toggle("active");
}

selectBtn.addEventListener("click", function (e) {
    e.stopPropagation();
    toggleMenu();
});

document.addEventListener("click", function (e) {
    const target = e.target;
    const its_menu = target == optionMenu || optionMenu.contains(target);
    const its_btnMenu = target == selectBtn;
    const menu_is_active = optionMenu.classList.contains("active");

    if (!its_menu && !its_btnMenu && menu_is_active) {
        toggleMenu();
    }
});
options.forEach(option =>{
    option.addEventListener("click", ()=>{
        let selectedOption = option.querySelector(".option-text").innerText;
        sBtn_text.innerText = selectedOption;
        let selectedOptionAttribyteQuerySelector = option.querySelector(".option-text");
        let selectedOptionAttribyte = selectedOptionAttribyteQuerySelector.dataset.type;
        fileinput.setAttribute("accept", selectedOptionAttribyte);

        const stn_text = document.querySelector(".sBtn-text");
        stn_text.classList.remove("blocked_text");
        blocked_button_task();
        optionMenu.classList.remove("active");
    });
});


fileinputContainer.addEventListener("mouseover", ()=> {
    const icon_file = document.querySelector('.bxl-dropbox');
    icon_file.classList.add("bx-tada");
});
fileinputContainer.addEventListener("mouseout", ()=> {
    const icon_file = document.querySelector('.bxl-dropbox');
    icon_file.classList.remove("bx-tada");
});

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