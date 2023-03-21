const upload_photo = document.querySelector(".input_upload_"),
save_photo = document.querySelector(".input_upload_save"),
input_upload_photo = document.querySelector(".upload-photo-file")

input_upload_photo.addEventListener('change', function(){
  if( this.value ){
    save_photo.classList.remove("save_photo");
    upload_photo.classList.add("change_photo")
  } else { 
  }
});

let popupBg = document.querySelector('.popup__bg');
let popup = document.querySelector('.popup');
let openPopupButtons = document.querySelector('.open-popup');
let closePopupButton = document.querySelector('.close-popup'); 


openPopupButtons.addEventListener('click', (e) => { 
    e.preventDefault(); 
    popupBg.classList.add('active'); 
    popup.classList.add('active'); 
});

closePopupButton.addEventListener('click',() => { 
    popupBg.classList.remove('active');
    popup.classList.remove('active'); 
});

document.addEventListener('click', (e) => { 
    if(e.target === popupBg) { 
        popupBg.classList.remove('active'); 
        popup.classList.remove('active'); 
    }
});