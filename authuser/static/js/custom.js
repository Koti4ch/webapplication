const standart_form = document.querySelector(".standart_form--input");
const btnk = document.querySelector("#console");



// standart_form.addEventListener("focus", function () {
//     if (standart_form.previousElementSibling.classList.contains("empty")) {
//         this.previousElementSibling.classList.toggle("empty");
//     };
//     if (!this.parentElement.classList.contains("cont")){
//         this.parentElement.classList.toggle("cont");
//     };
// })

// standart_form.addEventListener("blur", function () {
//     nullcontent(this);
// })

function tagCreator(tgt) {
    tgt.addEventListener("focus", function () {
        if (standart_form.previousElementSibling.classList.contains("empty")) {
            this.previousElementSibling.classList.toggle("empty");
        };
        if (!this.parentElement.classList.contains("cont")) {
            this.parentElement.classList.toggle("cont");
        };
    })

    tgt.addEventListener("blur", function () {
        nullcontent(this);
    })
};

function nullcontent(a) {
    if (a.value == "") {
        a.previousElementSibling.classList.toggle("empty");
        a.parentElement.classList.toggle("cont")
    };
};

standartInputs = document.querySelectorAll(".standart_form--input");
standartInputs.forEach(element => {
    element.addEventListener("focus", function () {
        if (this.previousElementSibling.classList.contains("empty")) {
            this.previousElementSibling.classList.toggle("empty");
        };
        if (!this.parentElement.classList.contains("cont")) {
            this.parentElement.classList.toggle("cont");
        };
    })

    element.addEventListener("blur", function () {
        nullcontent(this);
    })
}); 
