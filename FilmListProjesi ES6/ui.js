//------------------------------------------------------------------------------------------------------------



class UI{

    static addFilmToUI (newFilm){
        const filmList = document.getElementById("films");//tbody seçtim.
        filmList.innerHTML += `
            <tr>
                    <td><img src="${newFilm.url}" class="img-fluid img-thumbnail"></td>
                    <td>${newFilm.title}</td>
                    <td>${newFilm.director}</td>
                    <td><a href="#" id = "delete-film" class = "btn btn-danger">Filmi Sil</a></td>
                    </tr>
            </tr>
        `; 
    }//filmimi ekledim
    static clearInputs(element1,elemen2,element3){//Temizleme işlemi 
        element1.value = "";
        elemen2.value = "";
        element3.value = "";
    }
    static displayMessage(message,type){//Hangi mesajı yazdırmak istediğimiz ve bu mesajın tipi.
        const cardBody = document.querySelector(".card-body");//CardBody seçtim
        //Alert divini oluşturma.
        const div = document.createElement("div");//Element oluşturdum.
        div.className = `alert alert-${type}`;//Type içinde yazan.
        div.textContent = message;
        //CardBody'me bu çocuğu eklemem lazım.
        cardBody.appendChild(div);//Ekleme işlemi.
        //-------------------------------------------
        setTimeout(function(){//Alert mesajım çalıştıktan sonra silinme fonksiyonu.
            div.remove();
        },1000);
        //-------------------------------------------
    }
    static loadAllFilms(films){
        const filmList = document.getElementById("films");//tBody kısmını aldım.
        films.forEach(function(film){
            filmList.innerHTML +=` 
            <tr>
                <td><img src="${film.url}" class="img-fluid img-thumbnail"></td>
                <td>${film.title}</td>
                <td>${film.director}</td>
                <td><a href="#" id = "delete-film" class = "btn btn-danger">Filmi Sil</a></td>
            </tr>
            `; // Bu şekilde Storageden alıp eklemiş oldum.
        });
    }
    static deleteFilmFromUI(element){
        element.parentElement.parentElement.remove();//Ara yüzümden kaldırdım.
    }
    static clearAllFilmsFromUI(){
        const filmsList = document.getElementById("films");
        //filmsList = ""; bu 1.yöntem.Bu yavaş çalışan bir yöntem.
        while(filmsList.firstElementChild !== null){//Childe olduğu sürece.
            filmsList.firstElementChild.remove();
        }
    }
    
}


//------------------------------------------------------------------------------------------------------------



