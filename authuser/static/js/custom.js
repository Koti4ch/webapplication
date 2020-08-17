const standartInputs = document.querySelectorAll(".standart_form--input, .standart_form--select");
const textInArea = document.querySelector(".standart_text-area");
const aboutMeText = document.querySelector(".about-me");

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
if (aboutMeText != null){
    aboutMeText.addEventListener("keyup", function(){
        if (aboutMeText.innerText.length > 255) {
            aboutMeText.innerText = aboutMeText.innerText.slice(0, 254);
            window.alert('Вы превысили лимит в 255 символов!');
        }
        textInArea.value = aboutMeText.innerText;
    })
}

// change avatar logic
const avatar = document.querySelector(".character-img");
const fileDialog = document.querySelector(".avatara-input");
const changeAvatarBtn = document.querySelector(".change-btn");

if (changeAvatarBtn != null) {
    changeAvatarBtn.addEventListener("click", function(e) {
        fileDialog.click();
    })
}



// colorise taskmanager list
// ##############################################
let taskheaders = document.querySelectorAll('.setcolor');
let taskfooters = document.querySelectorAll('.setborder');
// ('1', 'Открыто'),
// ('2', 'В процессе выполнения'),
// ('3', 'Выполнено'),
// ('0', 'Удалено'),

function colorizeTask(tasklist) {
    tasklist.forEach(elem => {
        switch (elem.dataset.taskstatus) {
            case '0':
                if (elem.classList.contains('setcolor')) {
                    elem.classList.toggle('setcolor');
                    elem.classList.add('bg-danger');
                } else if (elem.classList.contains('setborder')) {
                    elem.classList.toggle('setborder');
                    elem.classList.add('border-danger');
                };
            case '2':
                if (elem.classList.contains('setcolor')) {
                    elem.classList.toggle('setcolor');
                    elem.classList.add('bg-warning');
                } else if (elem.classList.contains('setborder')) {
                    elem.classList.toggle('setborder');
                    elem.classList.add('border-warning');
                };
            case '3':
                if (elem.classList.contains('setcolor')) {
                    elem.classList.toggle('setcolor');
                    elem.classList.add('bg-success');
                } else if (elem.classList.contains('setborder')) {
                    elem.classList.toggle('setborder');
                    elem.classList.add('border-success');
                };
            case '1':
                if (elem.classList.contains('setborder')) {
                    elem.classList.toggle('setborder');
                    elem.classList.add('border-dark');
                };
        }
    });
}

colorizeTask(taskheaders);
colorizeTask(taskfooters);



// taskheaders.forEach(element => {
//     switch (element.dataset.taskstatus) {
//         case '0':
//             element.classList.toggle('setcolor');
//             element.classList.add('bg-danger');
//         case '2':
//             element.classList.toggle('setcolor');
//             element.classList.add('bg-warning');
//         case '3':
//             element.classList.toggle('setcolor');
//             element.classList.add('bg-success');
//     }
    // if (element.dataset.taskstatus == 0) {
    //     element.classList.toggle('setcolor');
    //     element.classList.add('bg-danger');
    // }
// });
