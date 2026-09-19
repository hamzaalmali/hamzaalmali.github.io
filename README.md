# Uygulama sitesi

Her uygulamanın bağımsız URL alanı vardır. Ortak ana sayfa yalnız katalogdur; uygulamaların gizlilik ve kullanım koşulları birbirine karıştırılmaz.

- `/foxplayer/`: Apple, Android, Smart TV ve masaüstü Fox Player
- `/netim/`, `/namaz-vakti/`, `/yedekleme-pro/`: mevcut bağımsız uygulamalar
- `/assets/site.css`: katalog ve Fox Player ortak görünümü
- `apps.json`: ana sayfadaki uygulamalar

## Yeni uygulama ekleme

1. Benzersiz küçük harfli bir klasör açın: örneğin `yeni-uygulama/`.
2. Bu klasöre `index.html`, `support.html`, `privacy.html`, `terms.html` ve gerekiyorsa `icon.png` ekleyin. Hukuki metinleri yeni uygulamanın gerçek veri işleme ve ödeme özelliklerine göre yazın; Fox Player metinlerini otomatik kopyalamayın.
3. `apps.json` dosyasına `slug`, `name`, `description`, `platforms` ve isteğe bağlı `icon` kaydı ekleyin.
4. `python3 scripts/build_catalog.py` çalıştırın. Bu işlem sadece ana katalog sayfasını üretir.
5. Değişiklikleri `main` dalına gönderin; GitHub Pages kök dizinden yayınlar.

## Fox Player mağaza adresleri

- Tanıtım: https://hamzaalmali.github.io/foxplayer/
- Destek: https://hamzaalmali.github.io/foxplayer/support.html
- Gizlilik: https://hamzaalmali.github.io/foxplayer/privacy.html
- Genel kullanım koşulları: https://hamzaalmali.github.io/foxplayer/terms.html
- Apple standart EULA: https://www.apple.com/legal/internet-services/itunes/dev/stdeula/

Apple mağaza açıklamalarında doğrudan Apple EULA bağlantısı korunmalıdır. Android ve TV sürümleri Fox Player genel koşullarına bağlanır. Mevcut mağaza bağlantılarını kırmamak için uygulama klasörlerini veya yayınlanmış hukuki belge yollarını yeniden adlandırmayın.
