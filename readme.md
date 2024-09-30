## Link Deployment
http://theresia-tarianingsih-wowlashopp.pbp.cs.ui.ac.id/

# Soal dan Jawaban Pertanyaan Tugas 4
1.  Apa perbedaan antara HttpResponseRedirect() dan redirect()
    ```HttpResponseRedirect()``` : argumen pertama yang digunakan hanya dapat berupa URL yang menghasilkan respons redirect sehingga dapat memuat ulang halaman URL
    ```redirect()``` : akan mengembalikan hasil dari ```HttpResponseRedirect()``` dapat menerima model, view, atau urls sebagau argumen tujuan sehingga lebih fleksibel (sumber: https://stackoverflow.com/questions/13304149/what-the-difference-between-using-django-redirect-and-httpresponseredirect)
2.  Jelaskan cara kerja penghubungan model Product dengan User!
     Cara penghubungan antara model Product dan User dilakukan menggunakan one to many field hal ini disebabkan karena satu user dapat memiliki banyak produk(dalam konteks website ini). dalam kode saya mengimplementasikannya dengan ```user = models.ForeignKey(User, on_delete=models.CASCADE)``` di models.py
3.  Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
    ```autentification```: untuk menentukan siapa(indentitas pengguna) yang sedang login apakah user dan passwordnya sudah benar atau belum
    ```authorization```: untuk menentukan roles user apa saja yang dapat user akses dan tidak dapat user akses
    Dalam Django kedua konsep ini adalah dengan mengimport ```from django.contrib.auth import authenticate, login``` ```from django.contrib.auth.decorators import login_required``` serta menambahkan decoration ```@login_required(login_url='/login')``` tidak lupa untuk mengimplementasikan fungsi ```def login_user(request):```
4.  Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
     Django mengingat penggunanya dengan menggunakan session cookies yang disimpan dalam browser. Dalam proyek Django digunakan ```login(request, user)```. Kegunaan lain dari cookies adalah untuk menyimpan data sementara serta mengingat preferensi pengguna sehingga iklan-iklan yang ditampilkan pada browser berdasarkan algoritma pencaharian pengguna. Tidak semua cookies aman, beberapa cookies akan menyebabkan beberapa ancaman masalah keamanan dan privasi.
5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
pertama saya membuat form register dengan mengimport ```UserCreationForm``` lalu saya membuat fungsi register pada ```views.py``` setelah itu saya membuat interface untuk register denan membuat file ```register.html``` setelah itu menambahkan path url register ke ```urls.py```. Setelah itu saya membuat fungsi login_user pada ```views.py``` lalu membuat interface login dengan membuat ```login.html``` setelah itu menambahkan path url loin pada ```urls.py```. setelah itu saya membuat fungsi logout_user pada ```views.py``` dan menambahkan button logout pada ```main.html``` serta menambahkan parth url logout pada ```urls.py``` setelah itu saya membuat restriksi login sehingga produk-produk toko hanya dapat diakses pada pemilik akun. lalu saya menyetin cookies untuk melihat aktivitas last login dan mengintegrasikan Product dengan User. setelah itu saya membuat migrasi dan push ke github. Tidak lupa saya run server terlebih dahulu di lokal sebelum dipush.

# Soal dan Jawaban Pertanyaan Tugas 5
 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
 terdapat 3 jenis selector pada CSS, yakni ```Element Selector``` yang berdasarkan pada tag HTML yang dimiliki seperti ```<body>, <h1>, <h2>``` pemanggilan pada CSS sama seperti nama tagnya, ```ID Selector``` yang menggunakan ID unik pada tag seperti ```<div id="text-bubble">``` pemanggilan pada CSS menggunakan format ```#[nama-id]```, dan```Class Selector``` yang memungkinkan kita untuk megelompokkan elemen dengan karakteristik yang sama seperti ```<div class="group-content">``` pemanggilan pada CSS menggunakan format ```.[nama-kelas]```. 
 Urutan prioritas(dari yang terpenting) pada CSS Selector ini adalah
        1. ```ID Selector``` karena spesifik pada ID yang unik
        2. ```Class Selector``` pada kelompok elemen tertentu
        3. ```Element Selector``` pada ta tertentu
 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
 Responsive design merupakan sistem desain web yang memiliki tujuan untuk menghasilkan tampilan web yang penataannya sesuai dengan berbagai ukuran perangkat, seperti desktop, mobile, tablet, dsb. Contoh yang sudah menerapkan responsive adalah ```https://pbp-fasilkom-ui.github.io/ganjil-2025/```, ```https://www.empoweruni.com/```, dan ```https://www.behance.net/```. Contoh aplikasi yang belum menerapkan responsive design adalah ```https://scele.cs.ui.ac.id/```,```https://academic.ui.ac.id/```,```https://siasisten.cs.ui.ac.id/```
 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
 ```margin```: merupakan ruang di luar border, margin berfungsi untuk menatur jarak antara elemen satu dengan yang lainnya
 ```border```: merupakan garis tepian yang membungkus konten dan paddingnya sehingga memberikan bingkai visual pada elemen
 ```padding```: ruang di dalam elemen dan border elemen sehingga konten tidak menempel langsung pada border
 Contoh implementasi dalam CSS:
 ```
 .element {
  margin: 20px;
  padding: 15px;
  border: 3px solid blue;
}
```
 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
 ```flex box```: merupakan sebuah tata letak pada sebuah dimensi yang digunakan untuk menyusun elemen dalam satu arah pada sumbu X atau sumbu Y. Flex box berguna jika kita hanya perlu menatur elemen secara sederhana dalam satu dimensi
 ```grid layout```: merupakan sebuah tata letak 2 dimensi yang dapat meletakkan elemen secara horizontal dan vertikal(membentuk baris dan kolom). Grid layout berguna jika kita ingin mengggunakan tata letak yang terdiri dari 2 dimensi
 
 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
 pertama saya mengimplementasi fitur edit product dan delete product pada views.py lalu mengintegrasikan masing-masing fungsi tersebut ke urls.py. setelah itu saya membuat html file untuk mengedit informasi product. setelah itu saya membuat konfigurasi untuk static files pada settings.py. Setelah itu saya menambahkan styles pada aplikasi dengan Tailwind dan css dengan menambahkan file global.css dan script tailwind ke base.html setelah itu saya styling halaman login, register, main, dan edit product. tak lupa saya turut membuat file stylin untuk card info product dan info user.

## Data Diri
Theresia Tarianingsih
2306208810 / PBP-C
