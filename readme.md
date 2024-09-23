## Link Deployment
http://theresia-tarianingsih-wowlashopp.pbp.cs.ui.ac.id/

# Soal dan Jawaban Pertanyaan
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

## Data Diri
Theresia Tarianingsih
2306208810 / PBP-C
