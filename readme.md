## Link Deployment
http://theresia-tarianingsih-wowlashopp.pbp.cs.ui.ac.id/

# Soal dan Jawaban Pertanyaan
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Penggunaan data delivery sangat penting dalam mengimplementasikan sebuah platform karena seluruh pengguna platform tentunya membutuhkan data sehingga dapat melakukan interaksi dengan platform. Platform memiliki beberapa layanan yang terintegrasi, maka dari itu data delivery membantu sinkronisasi data antara komponen-komponen yang ada pada platform.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik dibandingkan dengan XML karena JSON memiliki struktur yang lebih sederhana berkat fitur ```pretty print``` sedangkan XML memiliki sintaks yan lebih kompleks sehingga sulit dibaca secara visual. JSON juga lebih mudah diolah jika ingin dilakukan pengambilan data, hanya dengan menggunakan Javascript. Maka dari itu JSON lebih populer karena lebih mudah dipahami dan lebih mudah digunakan dalam pengembangan web.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
```is_valid()``` merupakan method yan digunakan untuk memeriksa validasi pada setiap field form program django. Method ini mereturn nilai boolean, mengembalikan True jika valid dan False jika tidak valid. Method ini diperlukan supaya memastikan daa-data yang diinput user sesuai dengan apa yang telah diprogram pada form.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
```CSRF_token``` digunakan untuk memastikan bahwa request yang dikirimkan pada server berasal dari user yang diinginkan. Jika tolen CSRF ini bernilai valid maka request akan segera diproses jika tidak, maka akan ditolak. Jika form pada project django tidak dilintungi oleh CSRF token maka website kita akan rentan untuk mendapatkan seranan Cross-Site Request Forgery sehingga keamanan website akan terancam. Penyerang mungkun saja membuat sebuah form yang mungkin bisa digunakan sebagai wadah untuk pencurian data pengguna web.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
pertama saya membuat sebuah direktori templates baru pada root folder lalu membuat berkas HTML baru yakni ```base.html``` sebagai template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web. Setelah itu saya mengedit ```settings.py``` lalu pada subdirektori main saya mengubah ```main.html``` lalu mengubah primary key pada ```models.py``` nebhjadi UUID sehingga menjaga keamanan web. Sebelum itu saya melakukan migrasi. Lalu saya membuat form input data yang menampilkan imput-imput produk yan dijual pada shop saya dengan method ```POST``` setelah itu saya mengubah context dan ```views.py``` sehingga dapat menampilkan halaman saat menambahkan form. Lalu menambahkan berkas html baru sebagai laman untuk mengisi input form dan menintegrasikannya denan ```main.html```. Setelah itu saya mencoba untuk mengintegrasikan masing-masing data dalam bentuk XML dan JSON. Lalu mencoba untuk bisa melihat data-data tersebut melalui PostMan. Lalu saya melakukan push ke github

# Screensshot Postman
mengakses xml
![Screenshot 2024-09-15 233301](https://github.com/user-attachments/assets/bedcab50-31bf-4f4c-81e9-7a5bfea825b4)
mengakses json
![Screenshot 2024-09-15 233619](https://github.com/user-attachments/assets/eb7a9971-ca76-45f1-b857-c03854e16432)
![Screenshot 2024-09-15 233632](https://github.com/user-attachments/assets/391800d8-e765-4d20-83ec-2e3daffc7f00)
mengakses xml by ID
![Screenshot 2024-09-15 233911](https://github.com/user-attachments/assets/d2d2fdc6-b7ea-4448-bb4c-11886560858f)
mengakses json by ID
![Screenshot 2024-09-15 233956](https://github.com/user-attachments/assets/49f25838-7afe-4975-bf46-fa88e58ab4ac)


## Data Diri
Theresia Tarianingsih
2306208810 / PBP-C
