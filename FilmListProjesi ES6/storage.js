//------------------------------------------------------------------------------------------------------------
class Storage{
    static addFilmToStorage(newFilm){
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
    static getFilmsFromStorage(){
        let films;
        if(localStorage.getItem("films")===null){//LocalStorage'de böyle bir key'im varmı kontrol ediyorum
            films=[];
        }
        else{//Eğer key'im varsa olan değerimi almam gerekiyor.
            films = JSON.parse(localStorage.getItem("films"));//String değerimi ARRAY haline çevirdim.
        }
        return films; //Fonksiyonumu geriye döndürdüm.
    }
    static deleteFilmFromStorage(filmTitle){
        let films = this.getFilmsFromStorage();
        films.forEach(function(film,index){//splice
            if(film.title === filmTitle) {
                films.splice(index,1);//Burda localStorage'den kaldırmıs oluyorum Filmimi.
            }
        });
        localStorage.setItem("films",JSON.stringify(films));//Sildiğim filmi localStorage yazdırdım.
    }
    static clearAllFilmsFromStorage(){
        localStorage.removeItem("films");
    }
    
}

//------------------------------------------------------------------------------------------------------------