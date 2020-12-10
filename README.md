# DES Encryption with simple interface
*** *There is an exe formatted application in the 'des_exe.zip' file.
    You can also use it to run the program directly.*

## How does it work ?

Encryption and decryption operations are carried out with the methods in 'DES_lib'
imported in 'DES_gui' where the code to run the program is located.
The data to be encrypted must be 8 bytes and its multiples, and the key must be net 8 bytes long.
In case this rule is broken, data and key are filled with PKCS5 padding method and encryption is done accordingly.
The user will not notice this and there will be no change in the output.
According to the DES algorithm, these keys and data are passed through SBOX permutations, a loop is created between blocks and this is repeated 16 times.

![DES_GUI](https://github.com/omerkocadayi/DES_Encryption/blob/main/DES_GUI.PNG)

## How to use ?

I simply designed an interface so that the program can be used comfortably.
This interface; input, output points and has operating buttons.
If 'Key' and 'Text' input fields are filled and 'RUN' button is activated,
The encryption algorithm will run and write the results in the section at the bottom of the interface.
If the 'Key' value is not entered, the key will be assigned as 'SAUCyber' by default.
If we want to encrypt a txt document, like the previous process, first of all the 'Key' value must be entered.
Then the 'RUN with TXT UPLOAD' button should be activated.
Thus, a screen will appear for you to select a 'TXT' document from your computer.
After selecting this document, the encryption algorithm will run again and create anew txt document
named 'DocumentName_CRYPTED' with the same file path as the document and write the results to this document.

*** *Ayrıca 'des_exe.zip' dosyasının içinde exe formatlı uygulama mevcut.
    Programı direkt olarak çalıştırmak için onu da kullanabilirsiniz.*

## Nasıl Çalışır ? 

Programı çalıştırma kodlarının bulunduğu 'Y205012105_RUN' içerisinde import edilen 'Y205012105_DES'in
içinde bulunan metodlar ile şifreleme ve şifre çözme işlemleri gerçekleşmektedir.
Şifrelenecek verilerin 8 bayt ve katları, anahtarın ise net 8 bayt uzunluğunda olması gerekmektedir.
Bu kuralın bozulması durumunda ise PKCS5 padding yöntemiyle veri ve anahtar doldurulup şifreleme ona göre yapılmaktadır.
Kullanıcı bunu fark etmeyecektir ve çıktılarında herhangi bir değişiklik olmayacaktır.
DES algoritması gereğince bu anahtar ve veriler SBOX permütasyonlarına uğratılır, bloklar arasında döngü oluşturulur ve bu 16 kez tekrarlanır.

## Nasıl Kullanılır ?

Programın rahatça kullanılabilmesi için basitçe bir arayüz tasarladım.
Bu arayüz; girdi,çıktı noktalarına ve çalıştırma butonlarına sahip.
'Key' ve 'Text' input alanları doldurulup 'RUN' butonu aktif edilirse,
şifreleme algoritması çalışacak ve arayüzün alt kısmında bulunan bölüme sonuçları yazacaktır.
'Key' değeri girilmemesi durumunda, key default olarak 'SAUCyber' olarak atanacaktır.
Eğer bir txt belgesi şifrelemek istiyorsak, az önceki işlem gibi ilk önce 'Key' değerinin girilmesi gerekmektedir.
Sonrasında ise 'RUN with TXT UPLOAD' butonu aktif edilmelidir.
Böylece karşınıza bilgisayarınızdan istediğiniz bir 'TXT' belgesini seçmeniz için bir ekran çıkacaktır.
Bu belgeyi seçtikten sonra şifreleme algoritması tekrar çalışacak ve belgeyle aynı dosya yoluna
sahip 'BelgeAdi_CRYPTED' adında yeni bir txt belgesi oluşturup sonuçları bu belgeye yazacaktır.
