const standartInputs = document.querySelectorAll(".standart_form--input, .standart_form--select");

// function tagCreator(tgt) {
//     tgt.addEventListener("focus", function () {
//         if (standart_form.previousElementSibling.classList.contains("empty")) {
//             this.previousElementSibling.classList.toggle("empty");
//         };
//         if (!this.parentElement.classList.contains("cont")) {
//             this.parentElement.classList.toggle("cont");
//         };
//     })

//     tgt.addEventListener("blur", function () {
//         nullcontent(this);
//     })
// };

function nullcontent(a) {
    if (a.previousElementSibling.classList.contains("not-empty") && a.value == ""){
        a.parentElement.classList.toggle("cont");
        return;
    };

    if (a.value == "") {
        a.previousElementSibling.classList.toggle("empty");
        a.parentElement.classList.toggle("cont");
    };
};


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
