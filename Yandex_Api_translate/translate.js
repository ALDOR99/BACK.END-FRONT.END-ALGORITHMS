//Burda api kullanımını gerçekleştirecem

//---------------------------------------------------------------------------------------------------------


function Translate(word,language){
    this.apiKey ="";
    this.word = word;
    this.language = language;

    //XHR objesi
    this.xhr = new XMLHttpRequest();
}
//Method ekleme
Translate.prototype.TranslateWlord = function(Callback){
    //Ajax işlemleri
    const endpoint = ``;
    this.xhr.open("GET",endpoint);
    this.xhr.onload = () => {
        if(this.xhr.status === 200){
            // console.log(this.xhr.responseText);
            const json = JSON.parse(this.xhr.responseText);
            const text = json.text[0];
            Callback(null,text);
        }else{
            Callback("Bir hata oluştu",null);
        }
    };
    this.xhr.send();
};
translate.prototype.changeParameters = function(newWord,newLanguage){
    this.word = newWord;
    this.language = newLanguage;
}

//---------------------------------------------------------------------------------------------------------

                                                                                                                                                      




























































































































































                                                                                                                                                                                                                                                                                                                                                        








                                                                                                                                                                                                                                                                                                                                                        















































































