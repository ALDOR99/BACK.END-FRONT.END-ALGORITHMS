//------------------------------------------------------------------------------------------------------------



const form = document.getElementById("film-form");//Film formu seçtim.
const titleElement = document.querySelector("#title"); 
const directorElement = document.querySelector("#director");
const urlElement = document.querySelector("#url");//Querylerimi seçtim.
const cardbody = document.querySelectorAll(".card-body")[1];//İkinci CardBody'mi aldım.
const clear = document.getElementById("clear-films");



//------------------------------------------------------------------------------------------------------------



//Tüm eventleri yükleme.
addEventListeners();
function addEventListeners(){//Tüm eventlerimi burda bağlıycam.
    
    form.addEventListener("submit",addFilm);//submit olduğunda fonksiyonumu çalıştırmasını istedim.
    document.addEventListener("DOMContentLoaded",function(){
        let films = Storage.getFilmsFromStorage();
        UI.loadAllFilms(films);
    });

    cardbody.addEventListener("click",deleteFilm);//Tıklandığında Silme fonksiyonu.
    clear.addEventListener("click",clearAllFims);//Tıklandığında tümü Silme fonksiyonu.
}



//------------------------------------------------------------------------------------------------------------



function addFilm(e){//Burda bize bir event objesi verecek.
    const title = titleElement.value;//Title değerimi aldım.
    const director = directorElement.value;//Director değerimi aldım.
    const url = urlElement.value//Url değerimi aldım.

    if(title === "" || director==="" || url===""){//Formum boş ise burda bir koşul sağlıyorum
        //hatta
        UI.displayMessage("Tüm alanları doldurun.","danger");//Hatta mesajımı yazdırdım.
    }
    else{
        //problem yok ise.
        //Yeni film.
        const newFilm = new Film(title,director,url);//Obje oluşturuyorum
        UI.addFilmToUI(newFilm);//Arayüze film ekleme.
        Storage.addFilmToStorage(newFilm);//Local Storage film ekleme.
        UI.displayMessage("Film Başarı İle Eklendi...","success");
    }
    UI.clearInputs(titleElement,urlElement,directorElement);//ClearInputumu burda çağırdım.İnputlarımdaki yazıyı sildim.
    e.preventDefault();//Formun submit edilmesini önlemek için.
}



//------------------------------------------------------------------------------------------------------------



function deleteFilm(e){
    if(e.target.id==="delete-film"){//İd delete-film tıklanırsa koşul çalışacak.
        UI.deleteFilmFromUI(e.target);
        Storage.deleteFilmFromStorage(e.target.parentElement.previousElementSibling.previousElementSibling.textContent);
        UI.displayMessage("Silme işlemi başarılı","success");//Bilgilendirme mesajı.
    }
}



//------------------------------------------------------------------------------------------------------------



function clearAllFims(){
    if(confirm("Emin misiniz ?")){
        UI.clearAllFilmsFromUI();
        Storage.clearAllFilmsFromStorage();
    }
}



//------------------------------------------------------------------------------------------------------------
























