
//Genel dosya
//Prototype,Ajax,Callback


//---------------------------------------------------------------------------------------------------------


addEventListeners();


//---------------------------------------------------------------------------------------------------------


function addEventListeners(){//Burda addEventListeners fonksiyonumu yazdım.
    document.getElementById("translate-form").addEventListener("submit",translateWord);//Submit olduğunda translateWord fonksiyonumu çalıştıracam.
    document.getElementById("language").onchange = function(){
        //Arayüz işlemleri
        ui.changeUI();
    }

}


//---------------------------------------------------------------------------------------------------------
const ui = new UI();
const translate = new Translate(document.getElementById("word").value,document.getElementById("language").value);

function translate(e){
    translate.changeParameters(document.getElementById("word").value,document.getElementById("language").value);
    translate.translateWord(function(err,response){
        if(err){
            console.log(err);
        }else{
            uı.displayTranslate(response);
        }
    });
    e.preventDefault();// Sayfamın yenilmesini engeledim.
}