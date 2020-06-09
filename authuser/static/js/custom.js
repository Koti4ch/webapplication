const standartInputs = document.querySelectorAll(".standart_form--input, .standart_form--select");
const textInArea = document.querySelector(".standart_text-area");
const aboutMeText = document.querySelector(".about-me");

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

// contenteditable DIV to textarea
aboutMeText.addEventListener("keyup", function(){
    if (aboutMeText.innerText.length > 255) {
        aboutMeText.innerText = aboutMeText.innerText.slice(0, 254);
        window.alert('Вы превысили лимит в 255 символов!');
    }
    textInArea.value = aboutMeText.innerText;
})