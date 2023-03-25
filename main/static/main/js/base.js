var confirmation_logout = document.getElementById("confirmation_logout"),
popupBg = document.querySelector('.popup__bg'),
popup = document.querySelector('.popup'),
body = document.getElementById("body"),
closePopupButton = document.querySelector('.close-popup'); 
confirmation_logout.addEventListener('click', () => { 
    popupBg.classList.add('active'); 
    popup.classList.add('active');
    body.style.overflow = "hidden"
});

closePopupButton.addEventListener('click', () => { 
    popupBg.classList.remove('active');
    popup.classList.remove('active');
    body.style.overflow = "auto" 
});

document.addEventListener('click', (e) => { 
    if(e.target === popupBg) { 
        popupBg.classList.remove('active'); 
        popup.classList.remove('active');
        body.style.overflow = "auto"
    }
});

const header_burger = document.querySelector(".header_burger-btn"),
menu_bar = document.querySelector('.menu-bar'),
blackout = document.querySelector(".blackout"),
sidebar = document.querySelector(".sidebar");
header_burger.addEventListener("click", () => {
    if(menu_bar.classList.contains("open")){
        menu_bar.classList.remove("open");
        blackout.classList.remove("open");
        sidebar.classList.remove("open");
    } else {
        menu_bar.classList.add("open");
        blackout.classList.add("open");
        sidebar.classList.add("open");
    }
});

// document.addEventListener("DOMContentLoaded", () => {
//     const windоwWidht = window.innerWidth;
//     console.log(windоwWidht);
//     if(windоwWidht < 800){
//         menu_bar.innerHTML = `
//         <div class="menu">
//             <ul class="menu-links">
//                 <li class="nav-link">
//                     <a href="{% url 'home' %}">
//                         <i class='bx bx-home-alt icon' ></i>
//                         <span class="text nav-text">Главная</span>
//                     </a>
//                 </li>
//                     <li class="nav-link">
//                         <a href="{% url 'top' %}">
//                             <i class='bx bx-bar-chart-alt-2 icon' ></i>
//                             <span class="text nav-text">Топ</span>
//                         </a>
//                     </li>
//                     <!-- <li class="nav-link">
//                         <a href="#">
//                             <i class='bx bx-heart icon' ></i>
//                             <span class="text nav-text">Друзья</span>
//                         </a>
//                     </li> -->
//                     <li class="nav-link">
//                         <div class="blocked">
//                             <i class='bx bxs-dizzy icon'></i>
//                             <span class="text">Друзья</span>
//                         </div>
//                     </li>
//                     <li class="nav-link">
//                         <a href="{% url 'competitions' %}">
//                             <i class='bx bx-math icon'></i> 
//                             <span class="text nav-text">Соревнования</span>
//                         </a>
//                     </li>
//                     <div class="bottom-content var cursor-p">
//                         <li class="">
//                             <a id="confirmation_logout">
//                                 <i class='bx bx-log-out icon' ></i>
//                                 <span class="text nav-text">Выйти</span>
//                             </a>
//                         </li>
//                     </div>
//             </ul>
//         </div>
//             <button class="header_burger-btn">
//                 <span></span><span></span><span></span>
//             </button>`;
//     } else {
//         menu_bar.innerHTML = `
//             <div class="menu">
//                 <ul class="menu-links">
//                     <li class="nav-link">
//                         <a href="{% url 'home' %}">
//                             <i class='bx bx-home-alt icon' ></i>
//                             <span class="text nav-text">Главная</span>
//                         </a>
//                     </li>
//                     <li class="nav-link">
//                         <a href="{% url 'top' %}">
//                             <i class='bx bx-bar-chart-alt-2 icon' ></i>
//                             <span class="text nav-text">Топ</span>
//                         </a>
//                     </li>
//                     <li class="nav-link">
//                         <div class="blocked">
//                             <i class='bx bxs-dizzy icon'></i>
//                             <span class="text">Друзья</span>
//                         </div>
//                     </li>
//                     <li class="nav-link">
//                         <a href="{% url 'competitions' %}">
//                             <i class='bx bx-math icon'></i> 
//                             <span class="text nav-text">Соревнования</span>
//                         </a>
//                     </li> 
//                 </ul>
//             </div>
//             <div class="bottom-content var cursor-p">
//                 <li class="">
//                     <a id="confirmation_logout">
//                         <i class='bx bx-log-out icon' ></i>
//                         <span class="text nav-text">Выйти</span>
//                     </a>
//                 </li>
//             </div>
//             <button class="header_burger-btn">
//                 <span></span><span></span><span></span>
//             </button>`;
//     };
//     confirmation_logout = document.getElementById("confirmation_logout");
//     console.log(confirmation_logout);
// });
// window.addEventListener('resize', () => {
//     const windоwWidht = window.innerWidth;
//     console.log(windоwWidht);
//     if(windоwWidht < 800){
//         menu_bar.innerHTML = `
//         <div class="menu">
//             <ul class="menu-links">
//                 <li class="nav-link">
//                     <a href="{% url 'home' %}">
//                         <i class='bx bx-home-alt icon' ></i>
//                         <span class="text nav-text">Главная</span>
//                     </a>
//                 </li>
//                     <li class="nav-link">
//                         <a href="{% url 'top' %}">
//                             <i class='bx bx-bar-chart-alt-2 icon' ></i>
//                             <span class="text nav-text">Топ</span>
//                         </a>
//                     </li>
//                     <li class="nav-link">
//                         <div class="blocked">
//                             <i class='bx bxs-dizzy icon'></i>
//                             <span class="text">Друзья</span>
//                         </div>
//                     </li>
//                     <li class="nav-link">
//                         <a href="{% url 'competitions' %}">
//                             <i class='bx bx-math icon'></i> 
//                             <span class="text nav-text">Соревнования</span>
//                         </a>
//                     </li>
//                     <div class="bottom-content var cursor-p">
//                         <li class="">
//                             <a id="confirmation_logout">
//                                 <i class='bx bx-log-out icon' ></i>
//                                 <span class="text nav-text">Выйти</span>
//                             </a>
//                         </li>
//                     </div>
//             </ul>
//         </div>
//             <button class="header_burger-btn">
//                 <span></span><span></span><span></span>
//             </button>`;
//     } else {
//         menu_bar.innerHTML = `
//             <div class="menu">
//                 <ul class="menu-links">
//                     <li class="nav-link">
//                         <a href="{% url 'home' %}">
//                             <i class='bx bx-home-alt icon' ></i>
//                             <span class="text nav-text">Главная</span>
//                         </a>
//                     </li>
//                     <li class="nav-link">
//                         <a href="{% url 'top' %}">
//                             <i class='bx bx-bar-chart-alt-2 icon' ></i>
//                             <span class="text nav-text">Топ</span>
//                         </a>
//                     </li>
//                     <!-- <li class="nav-link">
//                         <a href="#">
//                             <i class='bx bx-heart icon' ></i>
//                             <span class="text nav-text">Друзья</span>
//                         </a>
//                     </li> -->
//                     <li class="nav-link">
//                         <div class="blocked">
//                             <i class='bx bxs-dizzy icon'></i>
//                             <span class="text">Друзья</span>
//                         </div>
//                     </li>
//                     <li class="nav-link">
//                         <a href="{% url 'competitions' %}">
//                             <i class='bx bx-math icon'></i> 
//                             <span class="text nav-text">Соревнования</span>
//                         </a>
//                     </li> 
//                 </ul>
//             </div>
//             <div class="bottom-content var cursor-p">
//                 <li class="">
//                     <a id="confirmation_logout" class="confirmation_logout1">
//                         <i class='bx bx-log-out icon' ></i>
//                         <span class="text nav-text">Выйти</span>
//                     </a>
//                 </li>
//             </div>
//             <button class="header_burger-btn">
//                 <span></span><span></span><span></span>
//             </button>`;
//             return confirmation_logout = document.querySelector("confirmation_logout1");
// //     console.log(confirmation_logout);
//     };
// });
