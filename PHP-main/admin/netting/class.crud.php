<?php 
session_start();                //session oturumunu baslatim
require_once("dbconfig.php");   //dbconfig dosyamı dahil etim.
                                //  Creat Read Update Delete
class crud{                     //veri tabani degiskeni
    private $db;                //db degiskeni
    private $dbhost=DBHOST;
    private $dbuser=DBUSER;
    private $dbpass=DBPWD;
    private $dbname=DBNAME;
        
    
    function __construct(){     //yapıcı method olusturdum
        try {//dene                   //veri tabani baglanti islemleri

            $this->db=new PDO('mysql:host='.$this->dbhost.';dbname='.$this->dbname.';charset=utf8', $this->dbuser, $this->dbpass);
            echo "Baglantı Başarılı";

        }catch(Exception $e){                                //try'da hata varsa eger    
            die("Bağlantı Başarısız:".$e->getMessage());    //programı durdur ve exception sınıfının uretıgı hatayı ekrana bas
        }
    }

    public function adminsLogin($admins_username,$admin_pass,$remember_me){                             //public erişime her yerden acik
                                                                                                        //kullanici adi diğeri kullanici sifresi
        try{                                                                                            //olasi bir işlem hatasi varsa Exception sinifindan donen hattayi gosterecem
            $stmt=$this->db->prepare("SELECT * FROM admins WHERE admins_username=? AND admins_pass=?"); //göstergeli soru isareti sorgumu olusturdum
                                                                        //burda bir kontrol yapiyorum
            if (isset($_COOKIE['adminsLogin'])) {                       //adminsLogin doluysa
                $stmt->execute([$admins_username,md5(openssl_decrypt($admin_pass,"AES-128-ECB","admins_coz"))]); 
            }else{                                                      //degilse
                $stmt->execute([$admins_username,md5($admin_pass)]);    //execute ile baslatiyorum,verilerimi dizi olarak gonderiyorum  
                                                                        //md5'ten gecirerek karsilastirma islemini yapıyorum   
            }                                                                       
            if($stmt->rowCount()==1){                                   //$stmt sorgusunda yapilan isleminde 1den fazla deger varsa yukardaki sorgu islemi basarili
                $row=$stmt->fetch(PDO::FETCH_ASSOC);                    //sutuna gore veri cekme islemi yaptim
                $_SESSION["admins"]=[                                                   //burda dizi seklinde session baslatim,anahtar degerlerle dizi olusturdum
                                    "admins_username"=>$admins_username,                //sessiona 1.degerimi atadim
                                    "admins_namesurname"=> $row['admins_namesurname'],  //sessiona 2.degerimi atadim
                                    "admins_file"=>$row['admins_file'],                 //sessiona 3.degerimi atadim
                                    "admins_id"=>$row['admins_id']                      //sessiona 4.degerimi atadim
                                ];
                
                if(!empty($remember_me) AND empty($_COOKIE['adminsLogin'])){            // eger remember_me bos degilse

                    $admins=
                            [
                                "admins_username" => $admins_username,
                                "admins_pass" => openssl_encrypt($admin_pass,"AES-128-ECB","admins_coz")    //AES-128-ECB = 128 bitlik sifreleme
                            ];

                    setcookie("adminsLogin",json_encode($admins),strtotime("+30 day"),"/");     //cookie'de saklama
                }else if(empty($remember_me)){                                                  // bossa remember_me
                    setcookie("adminsLogin",json_encode($admins),strtotime("-30 day"),"/");
                }
                return ['status'=>TRUE];                                 //status,degeri true dizi olarak dondurdum
            }else{                                                       //islem basarisizsa 
                return ['status'=>FALSE];                                //status,degeri false dizi olarak dondurdum
            }
        }catch(Exception $e){                                            //kodlarimda hata varsa catch kismi calisacak
            return ['status'=> FALSE,'error'=>$e->getMessage()];         //donen hatayi exception sinifi ile aliyorum
        }
    }
}






?>