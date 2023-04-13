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