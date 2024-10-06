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

# Soal dan Jawaban Pertanyaan Tugas 6
 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
 Melalui JavaScript dapat memanipulsi halaman web secara dinamis serta interaksi antara halaman web dapat dilakukan dengan maksimal, selain itu JavaScript memungkinkan untuk mempercepat waktu respons aplikasi
 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
 await digunakan untuk menunggu hasil dari fetch. ketika menggunakan fetch() kita memulai proses request http dengan cara asinkronus lalu dengan await kita menunggu proses fetch selesai dan hasilnya tersedia sebelum beralih ke eksekusi berikutnya. Jika kita tidak menggunakan await maka java script akan melanjutkan eksekusi kode tanpa menunggu hasil dari fetch sehingga terjadi overlap pada penyimpanan variabel yang seharusnya menyimpan hasil permintaan yang diinginkan dan hasil yang dikeluarkan tidak sesuai dengan ekpektasi
 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
 CSRF merupakan sebuah serangan keamanan yang terjadi ketika permintaam yang tidak valid dikirim ke server dari pengguna yang telah terautentifikasi, sehingga decorator csrf_exempt digunakan untuk mengecualikan pemeriksaan token CSRF pada view yang menggunakan AJAX POST request. Jika tidak menggunakan csrf_exempt permintaan dari AJAX POST akan ditolak karena pelanggaran CSRF
 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
 Hal ini disebabkan karena untuk keamanan dari data, karena jika pembersian data dilakukan pada frontend maka bisa saja pengguna memanipulasi kode yang kita miliki.
 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
 pertama saya menambahkan error message pada aktifitas login yang gagal dengan menambahlam else yang berisi ```messages.error(request, "Invalid username or password. Please try again.")``` pada ```if form.is_valid()```. Setelah itu saya membuat fungsi untuk menambahkam product ```add_product_ajax``` dengan menggunakan AJAX dengan menambahkan decorator ```@csrf_exempt``` dan ```@require_POST``` lalu pada variabel name dan description saya menambahkan strip_tags untuk menghilangkan tag HTML yang terdapat pada data yang dikirimkan pengguna dengan request POST. setelah itu saya melakukan routing fungsi ```add_product_ajax``` pada ```urls.py``` lalu saya melakukan fetching dari data-data product yang telah dimiliki user. Lalu saya membuat fungsi pada block script ```refreshProductEntries()``` tidak lupa untuk menambahkan cost name dan cont description untuk membersihkan data yan diPOST dan menyesuaikan htmlString dengan card yang saya desain. Lalu saya membuat modal untuk menambahkan product dengan ajax. Lalu supaya modal tersebut masih berfungsi saya membuat fungsi ```showModal()``` dan ```hideModal()```. lalu menambahkan button add product by ajax dengan targetnya curdModal. Setelah itu kita menambahkan fungsi ```addProductEntry()``` dengan method post lalu memanggil fungsi ```refreshProductEntries()``` dan menambahkan event listener pada form yang ada di modal denan memanggil ```addProductEntry()```. Lalu saya menambahkan fungsi ```clean_name()``` dan ```clean_desc``` pada form.py. Lalu pada berkas main.html di dalam block meta saya menambahkan script ```<script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>```

## Data Diri
Theresia Tarianingsih
2306208810 / PBP-C
