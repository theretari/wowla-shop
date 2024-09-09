## Link Deployment
http://theresia-tarianingsih-wowlashop.pbp.cs.ui.ac.id/

# Soal dan Jawaban Pertanyaan
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Untuk membuat sebuah program django langkah pertama yang saya lakukan adalah dengan membuat sebuah direktori utama yakni dengan nama "wowla-shop" setelah itu saya membuat virtual environment dan mengaktivasi virtual environment supaya tidak bertabrakaan dengan komputer. Setelah itu saya meninstal django dan membuat project "wowla_shop" lalu saya melakukan konfigurasi proyek dan menjalankan project django terlebih dahulu sebelum lanjut ke langkah selanjutnya tidak lupa saya menonaktifkan server dan environment. setelah itu saya melakukan push yang pertama untuk mengirim seluruh berkas-berkas direktori yang telah saya buat. Setelah itu saya membuat berkas ".gitignore" sebagai sebuah berkas konfigurasi yan digunakan di dalam repositori git yang dimana berguna untuk memilih berkas yang harus diabaikan. Setelah itu saya kembali mengaktifkan enviroment dan membuat aplikasi baru dengan nama "main". Lalu saya menambahkan aplikasi main ke dalam proyek dengan menambahkan sejumlah kode di dalam file setings.py Setelah itu saya membuat berkas html sebaai template di dalam aplikasi lalu menubah berkas models.py dalam aplikasi sesuai dengan ketentuan soal. Tidak lupa saya melakukan migrasi model sehingga jika terdapat sebuah perubahan dapat dikenali oleh server. Setelah itu saya melakukan integrasi model, views, dan template di berkas "views.py" dan memperbaiki struktur berkas html sehina dapat terintegrasi dengan variabel-variabel yang ada di views.py. Setelah itu saya melakukan routing URL aplikasi dengan menuliskan sejumlah kode di "urls.py" yang di dalam direktori main. Setelah itu saya mengecek website saya melalui local host dengan menjalankan server django.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![URLS](https://github.com/user-attachments/assets/e3916544-0229-40f8-8056-80f460583802)
Bagan tersebut merupakan konsep dan arsitektur pada Django yang menggunakan konsep MVT. Saat client mengirimkan request ke internet maka internet melakukan request kepada file django untuk komponen-komponen MVT ini. MVT itu sendiri adalah

```Model```     : bertanggung jawab untuk mengatur dan mengelola seluruh data pada aplikasi. Model mewakili struktur data dan logika aplikasi di belakang tampilan web.
```View```      : komponen yang menangani logika presentasi dalam konsep MVT. View mengontrol bagaimana data yang dikelola oleh model dapat ditampilkan oleh pengguna
```Template```  : mengatur tampilan interface pengguna dengan memisahkan kode HTML dari loika aplikasi

3 hal ini saling berkaitan dalam bekerjanya sebuah website.

4. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git berfungsi sebagai sistem kontrol yang melacak perubahan kode yang dibuat oleh programmer. Melalui git kita dapat melacak seluruh perubahan proyek yang dilakukan seiring waktu namun git memiliki peran yang penting pada saat pengembangan proyek berskala besar dan secara berkolaborasi dengan orang lain(secara tim)

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Umumnya pada saat orang-orang baru pertama kali mempelajari bahasa pemrograman, tentunya mereka mempelajari bahasa python sebagai fundamental pemograman mereka. Jika seiring waktu ingin mempelajari bagaimana cara membangun sebuah website, django merupakan pilihan yang cocok karena berdasarkan dari bahasa pemograman python sehingga lebih mudah untuk dimengerti oleh pemula dengan bahasa yang simple. Selain itu django dilengkapi dokumentasi yang lengkap sehingga mempermudah untuk dipelajari.

6. Mengapa model pada Django disebut sebagai ORM?
Hal ini disebabkan karena model pada django memiliki fungsi sebagai penghubung ke database tanpa adanya keterlibatan SQL secara langsung. Integrasi data pada django sudah dicover oleh model itu sendiri

## Data Diri
Theresia Tarianingsih
2306208810 / PBP-C
