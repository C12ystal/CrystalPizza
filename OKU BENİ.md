# CrystalPizza
A project made for Global AI Hub

Projeyi açtıktan sonra karşınıza 4 farklı menü tuşu ve bir tane kapama tuşu çıkacaktır

--- Pizzalar ---

Pizza menüsüne girip istediğiniz pizzayı seçebilir ve seçtikten sonra karşınıza gelen ekranda istediğiniz gibi şekillendirebilirsiniz.
Custom pizza dışındaki bütün pizzalar bazı başlangıç malzemeleri ile gelir ve bu malzemeler dışında malzeme eklenemez
örn: Lahmacuna mantar ekleyemezsiniz -Bu custom pizzanın daha cazip hale gelmesini sağlar çünkü her malzeme açıktır-
Pizzada yapılan herhangi bir değişiklik pizzanın açıklamasında gösterilir ve ekranın sağında bulunan fiyat göstergesine yansıtılır.
Her malzemenin belli bir fiyatı vardır ve bir liste halinde tutulur, fiyatlandırma custom pizza için 40'tan diğer pizzalar için 20'den başlar
Malzemenin yokluğu onu fiyattan kaldırırken ekstra oluşu fiyatını 1.5 katına çıkarır.
Custom pizzada olmayan bir malzeme açıklamasına özellikle eklenmezken diğer pizzalarda eklenir örn: Soğansız Lahmacun olabilir ama Soğansız Custom olmaz
çünkü custom pizzanın bir başlangıç formu yoktur.
Sadece sos seçemezsiniz! Pizzanın üzerinde sos dışında en az bir malzeme olmalıdır, sadece sosla devam etmeyi denerseniz sistem devam etmenize izin vermeyecektir.
İstediğiniz zaman "Go Back" tuşuna basarak pizza seçme ekranına geri dönebilirsiniz veya "Add to Cart" tuşuna basarak hazırladığınız pizzayı sepetinize ekleyebilirsiniz.
"Add to Cart" tuşuna bastıktan sonra pizza seçme ekranına geri dönersiniz ve siparişinize daha fazla pizza ekleyebilirsiniz.

--- İçecekler ---

Karşınıza çıkan içecek listesinden istediğinize tıklayarak 1 litre tekrar tıklayarak 2.5'litrelik içecek seçebilir, "Go Back" ve "Add to Cart" tuşlarını kullanabilirsiniz.
Aynı içecekten birden fazla sipariş vermek için add to cart dedikten sonra içecek ekranına tekrar dönüp aynı şeyi seçerek sepetinize eklerseniz 2. defa sepetinize ekler
ve fiyata yansıtır.

--- Tatlılar ---

İçecekler ekranında yaptığınız şeylerin aynısını burdada yapabilirsiniz, tek farkı 1 litre ve 2.5 litre seçenekleri yerine 1 porsiyon ve 2 porsiyon seçenekleridir.

--- Checkout ---

Karşınıza gelen ekranın sağ tarafında siparişinizin detayları, ortasında işlem tuşları bulunur; sol tarafında ise sizden bilgileriniz alınır.
"Go Back" tuşuna basarak ana menüye geri dönebilirsiniz
"Clear Cart" tuşuna bastığınızda size emin misiniz diye sorar, tekrar bastığınızda ise sepetinizi temizler ve bulunduğunuz ekranı yeniler.
Bu işlem girdiğiniz bilgilerin silinmesine sebep olur!

Bilgilerinizi doldurup "Make Purchase" tuşuna bastığınızda:
  Verdiğiniz bilgilerin geçerli olup olmadığı kontrol edilir
  
  Siparişi bitirebilmek için gereken şartlar:  
    Siparişinizde en az 1 pizza bulunmalıdır -sonuçta pizzacıdasınız-.
    
    Girdiğiniz bilgiler geçerli olmalıdır:
      Bilgilerin hepsi sayılardan oluşmalıdır, herhangi birinin içinde harf bulunamaz.
      Bilgilerin her biri kendi karakter sayısına uymalıdır -Tc=11, Kart No=16, CCV=3, Kart Şifresi>=4-.

Yukarıda Görülen şartlardan herhangi birinin karşılanmaması durumunda siparişinizi bitiremezsiniz.
Sistem size şartlardan hangilerini karşılamadığınızı her "Make Purchase" tuşuna bastığınızda sırayla söyleyecektir.
Bütün şartları karşıladıktan sonra "Make Purchase" tuşuna basarsanız sistem siparişinizi tamamlar ve kendini kapatır.
Siparişiniz cart.txt dosyasına tarihi ile birlikte işlenir.
