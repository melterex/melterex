const upload_photo = document.querySelector(".input_upload_"),
save_photo = document.querySelector(".input_upload_save"),
input_upload_photo = document.querySelector(".upload-photo-file")
console.log(upload_photo, save_photo, input_upload_photo)

input_upload_photo.addEventListener('change', function(){
  if( this.value ){
    save_photo.classList.remove("save_photo");
    upload_photo.classList.add("change_photo")
  } else { 
  }
});

let popupBg2 = document.querySelector('.pbg2');
let popup2 = document.querySelector('.p2');
let openPopupButtons2 = document.querySelector('.op2');
let closePopupButton2 = document.querySelector('.cp2'); 


openPopupButtons2.addEventListener('click', (e) => { 
    e.preventDefault(); 
    popupBg2.classList.add('active'); 
    popup2.classList.add('active'); 
});

closePopupButton2.addEventListener('click',() => { 
    popupBg2.classList.remove('active');
    popup2.classList.remove('active'); 
});

document.addEventListener('click', (e) => { 
    if(e.target === popupBg2) { 
        popupBg2.classList.remove('active'); 
        popup2.classList.remove('active'); 
    }
});