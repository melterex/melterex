var count = document.querySelectorAll('.string').length;
var cnt = 20;
var cnt_page = Math.ceil(count / cnt);

var paginator = document.querySelector(".paginator");
function create_button(){
    var page = "";
    for (var i = 0; i < cnt_page; i++) {
  page += "<span class='pagination_button paginator_pasive' data-page=" + i * cnt + "  id=\"page" + (i + 1) + "\">" + (i + 1) + "</span>";
}
paginator.innerHTML = page;
var main_page = document.getElementById("page1");
main_page.classList.remove("paginator_pasive");
main_page.classList.add("paginator_active");
}
create_button();
var main_page = document.getElementById("page1");
function ne_otobchachenie() {
    for (var i = 0; i < div_num.length; i++) {
  if (i < count) {
    div_num[i].style.display = "none";
  }
}
}
function otobrachenie() {
    for (var i = 0; i < div_num.length; i++) {
  if (i < cnt) {
    div_num[i].style.display = "";
  }
}
}
var div_num = document.querySelectorAll(".string");
otobrachenie();

var main_page = document.getElementById("page1");
main_page.classList.remove("paginator_pasive");
main_page.classList.add("paginator_active");


function pagination(event) {
  var main_page_main = document.querySelectorAll(".pagination_button");
  var e = event || window.event;
  var target = e.target;
  var id = target.id;
  
  if (target.tagName.toLowerCase() != "span") return;
  
  var num_ = id.substr(4);
  var data_page = +target.dataset.page;
  for(var i = 0; i < main_page_main.length; i++){
    main_page_main[i].classList.add("paginator_pasive");
  }
  main_page.classList.remove("paginator_active");
  main_page = document.getElementById(id);
  main_page.classList.remove("paginator_pasive");
  main_page.classList.add("paginator_active");

  var j = 0;
  for (var i = 0; i < div_num.length; i++) {
    var data_num = div_num[i].dataset.num;
    if (data_num <= data_page || data_num >= data_page)
      div_num[i].style.display = "none";

  }
  for (var i = data_page; i < div_num.length; i++) {
    if (j >= cnt) break;
    div_num[i].style.display = "";
    j++;
  }
}
let inputBox = document.querySelector(".search_container"),
            searchIcon = document.querySelector(".icon_"),
            closeIcon = document.querySelector(".bx-x");

        searchIcon.addEventListener("click", () => inputBox.classList.add("open"));
        closeIcon.addEventListener("click", () => {
            inputBox.classList.remove("open");
            document.querySelector('#elastik').value = ""
            let elastikItems = document.querySelectorAll('.elastik tr');
            elastikItems.forEach(function (elem) {
                    let elem_itemms = elem.querySelector('.position__user')
                    elem.style.display = "none";

                    elem_itemms.innerHTML = elem_itemms.innerText;
                });
                otobrachenie();
                create_button();
        });

        document.querySelector('#elastik').oninput = function () {
            let val = this.value.trim();
            let elastikItems = document.querySelectorAll('.elastik tr');
            var main_page_main = document.querySelectorAll(".pagination_button");
            if (val != '') {
                ne_otobchachenie();
                console.log(paginator);
                if(main_page_main.length != 0){
                    for(var i = 0; i < cnt_page; i++){
                        console.log(main_page_main);
                    main_page_main[i].remove()
                };
                }
                elastikItems.forEach(function (elem) {
                    let elem_itemms = elem.querySelector('.position__user');
                    let elem_itemms_upper = elem_itemms.textContent.toLowerCase();
                    console.log(elem_itemms_upper)
                    if (elem_itemms_upper.search(val.toLowerCase()) == -1) {
                        elem.style.display = "none";
                    }
                    else {
                        elem.style.display = "";
                        let str = elem_itemms.innerText;
                    }
                });
            }
            else {
                ne_otobchachenie();
                otobrachenie();
                create_button();
            }
        }