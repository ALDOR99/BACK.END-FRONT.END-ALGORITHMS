//------------------------------------------------------------------------------------------------------------



const form = document.getElementById("film-form");//Film formu seçtim.
const titleElement = document.querySelector("#title"); 
const directorElement = document.querySelector("#director");
const urlElement = document.querySelector("#url");//Querylerimi seçtim.
const cardbody = document.querySelectorAll(".card-body")[1];//İkinci CardBody'mi aldım.
const clear = document.getElementById("clear-films");



//------------------------------------------------------------------------------------------------------------



//UI objesini başlatma.
const ui = new UI();



//------------------------------------------------------------------------------------------------------------



//Storage Objesi Üret.
const storage = new Storage();


//------------------------------------------------------------------------------------------------------------



//Tüm eventleri yükleme.
addEventListeners();
function addEventListeners(){//Tüm eventlerimi burda bağlıycam.
    
    form.addEventListener("submit",addFilm);//submit olduğunda fonksiyonumu çalıştırmasını istedim.
    document.addEventListener("DOMContentLoaded",function(){
        let films = storage.getFilmsFromStorage();
        ui.loadAllFilms(films);
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
        ui.displayMessage("Tüm alanları doldurun.","danger");//Hatta mesajımı yazdırdım.
    }
    else{
        //problem yok ise.
        //Yeni film.
        const newFilm = new Film(title,director,url);//Obje oluşturuyorum
        ui.addFilmToUI(newFilm);//Arayüze film ekleme.
        storage.addFilmToStorage(newFilm);//Local Storage film ekleme.
        ui.displayMessage("Film Başarı İle Eklendi...","success");
    }
    ui.clearInputs(titleElement,urlElement,directorElement);//ClearInputumu burda çağırdım.İnputlarımdaki yazıyı sildim.
    e.preventDefault();//Formun submit edilmesini önlemek için.
}



//------------------------------------------------------------------------------------------------------------



function deleteFilm(e){
    if(e.target.id==="delete-film"){//İd delete-film tıklanırsa koşul çalışacak.
        ui.deleteFilmFromUI(e.target);
        storage.deleteFilmFromStorage(e.target.parentElement.previousElementSibling.previousElementSibling.textContent);
        ui.displayMessage("Silme işlemi başarılı","success");//Bilgilendirme mesajı.
    }
}



//------------------------------------------------------------------------------------------------------------



function clearAllFims(){
    if(confirm("Emin misiniz ?")){
        ui.clearAllFilmsFromUI();
        storage.clearAllFilmsFromStorage();
    }
}



//------------------------------------------------------------------------------------------------------------
























