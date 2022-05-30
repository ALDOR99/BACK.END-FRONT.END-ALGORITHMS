//------------------------------------------------------------------------------------------------------------
function Storage(){
                   
}
Storage.prototype.addFilmToStorage = function(newFilm){
    let films = this.getFilmsFromStorage();
    films.push(newFilm);//Ekledim.
    /*
    [
        {title:"sadsadsad",director:"asdasdsad",url:"321123"},
    ]
    ***Bu şekilde bir işlem oluyor yani obje yazmış oluyorum***
    */
   localStorage.setItem("films",JSON.stringify(films));//LocalStorage yazmış oldum.
}
Storage.prototype.getFilmsFromStorage = function(){
    let films;
    if(localStorage.getItem("films")===null){//LocalStorage'de böyle bir key'im varmı kontrol ediyorum
        films=[];
    }
    else{//Eğer key'im varsa olan değerimi almam gerekiyor.
        films = JSON.parse(localStorage.getItem("films"));//String değerimi ARRAY haline çevirdim.
    }
    return films; //Fonksiyonumu geriye döndürdüm.
}
Storage.prototype.deleteFilmFromStorage = function(filmTitle){
    let films = this.getFilmsFromStorage();
    films.forEach(function(film,index){//splice
        if(film.title === filmTitle) {
            films.splice(index,1);//Burda localStorage'den kaldırmıs oluyorum Filmimi.
        }
    });
    localStorage.setItem("films",JSON.stringify(films));//Sildiğim filmi localStorage yazdırdım.
}
Storage.prototype.clearAllFilmsFromStorage = function(){
    localStorage.removeItem("films");
}

//------------------------------------------------------------------------------------------------------------