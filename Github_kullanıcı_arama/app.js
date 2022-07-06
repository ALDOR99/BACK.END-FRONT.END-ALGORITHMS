//Ana Dosya
//------------------------------------------------------------------------------------


//Elementleri Seçme işlemleri.
const githubForm = document.getElementById("github-form");
const nameInput = document.getElementById("githubname");
const clearLastUsers = document.getElementById("clear-last-user");

const lastUsers = document.getElementById("last-users");//ul
const github = new Github();
const ui = new Uİ();
//------------------------------------------------------------------------------------


eventListeners();//Fonksiyon yazdım.


function eventListeners(){
    githubForm.addEventListener("submit",getData);  
    clearLastUsers.addEventListener("click",clearAllSearched);
    document.addEventListener("DOMContentLoaded",getAllSearched);
}


//------------------------------------------------------------------------------------


function getData(e){

    let username = nameInput.value();//Sağdaki ve soldaki gereksiz boşlukları siliyorum.
    if(username === ""){
        alert("Lütfen geçerli bir kullanıcı adı girin.");
    }
    else{
        github.getGithubData(username)
        .then(response=> {
            if(response.user.message === "Not Found"){
                ui.showError("Kullanıcı bulunamadı");
            }
            else{
                ui.addSearchedUserToUI(username);
                Storage.addSearchedUserToStorage(username);
                ui.showUserInfo(response.user); 
                ui.showRepoInfo(response.repo);
            }
        })
        .catch(err=>ui.showError(err)); 
    } 

    ui.clearInput(); // Input temizleme 
    e.preventDefault();//Sayfanın yenilenmemesi için.
}

//------------------------------------------------------------------------------------


function clearAllSearched(){
    //Tüm arananları temizle.
    if(confirm("Emin misiniz ?")){
        //Silme işlemlerimiz
        Storage.clearAllSearchedUserFromStorage();//Storagden temizleme
        ui.clearAllSearchedFromUI();
    }
}


//------------------------------------------------------------------------------------


function getAllSearched(){
    //Arananları al Uİ'ye ekle. 
    let users = Storage.getSearchedUsersFromStorage();
    let result="";//Boş string 
    users.forEach(user=>{
        result +=`<li class="list-group-item">${user}</li>`;
    });
    lastUsers.innerHTML = result;
}


//------------------------------------------------------------------------------------









