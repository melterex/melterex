const accordionContent = document.querySelectorAll(".block");

        accordionContent.forEach((item, index) => {
            let header = item.querySelector("header");
            header.addEventListener("click", () =>{
                item.classList.toggle("open");
        
                let description = item.querySelector(".text-1");
                if(item.classList.contains("open")){
                    description.style.height = `${description.scrollHeight + 15}px`; //scrollHeight property returns the height of an element including padding , but excluding borders, scrollbar or margin
                    item.querySelector("i").classList.replace("bx-rotate-270", "bx-rotate-90");
                }else{
                    description.style.height = "0px";
                    item.querySelector("i").classList.replace("bx-rotate-90", "bx-rotate-270");
                }
                removeOpen(index); //calling the funtion and also passing the index number of the clicked header
            })
        })
        
        function removeOpen(index1){
            accordionContent.forEach((item2, index2) => {
                if(index1 != index2){
                    item2.classList.remove("open");
        
                    let des = item2.querySelector(".text-1");
                    des.style.height = "0px";
                    item2.querySelector("i").classList.replace("bx-rotate-90", "bx-rotate-270");
                }
            })
        }