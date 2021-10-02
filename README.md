### MEMBUAT APLIKASI DENGAN NAMA 'IKLANKAN' MENGGUNAKAN DJANGO FRAMEWORK VERSI 3.2

Github:
https://github.com/gurnitha/django-iklankan

### ------------------------------------------------------
### 1. INISIAL SETUP
### ------------------------------------------------------


#### 1.1 Menginstall Python, membuat proyek direktori, README.md, .gitignore file dan lokal repository

        new file:   .gitignore
        new file:   README.md


### ------------------------------------------------------
### 2. MEMBUAT DJANGO PROYEK DAN APP
### ------------------------------------------------------


#### 2.1 Membuat virtual environment dengan nama 'venv3932'

        modified:   .gitignore
        modified:   README.md


#### 2.2 Menginstall Django v3.2

        Steps:

        1. Aktifkan venv3932
        2. Install django

        modified:   README.md        


#### 2.3 Meng-upgrade versi pip

        Steps:

        1. Upgrade pip
        2. Cek versi pip setelah di-upgrade

        modified:   README.md


#### 2.4 Membuat django proyek

        Steps:

        1. Cek perintah untuk membuat django proyek
        2. Membuat django proyek

        modified:   README.md
        new file:   manage.py
        new file:   proyek/__init__.py
        new file:   proyek/asgi.py
        new file:   proyek/settings.py
        new file:   proyek/urls.py
        new file:   proyek/wsgi.py


#### 2.5 Membuat django app

        Steps:

        1. Cek perintah untuk membuat django app
        2. Membuat direktori 'apps' dan main
        3. Membuat django app dgn nama 'main' di dalam direktori 'apps' => 'apps/main'

        modified:   README.md
        new file:   apps/main/__init__.py
        new file:   apps/main/admin.py
        new file:   apps/main/apps.py
        new file:   apps/main/migrations/__init__.py
        new file:   apps/main/models.py
        new file:   apps/main/tests.py
        new file:   apps/main/views.py
        modified:   proyek/settings.py


#### 2.6 Meregistrasi django app 'apps/main' pada proyek agar diketahui oleh proyek

        Steps:

        1. Re-name name pada apps.js dari name='main' => name='apps.main'
        2. Registrasi apps/main pada settings.py

        modified:   README.md
        modified:   apps/main/apps.py
        modified:   proyek/settings.py


### ------------------------------------------------------
### 3. MEMBUAT DATABASE DGN MANGGUNAKAN MYSQL
### ------------------------------------------------------


#### 3.1 Membuat database

        Steps:

        1. Mengistall 'mysqlclient' package
        2. Membuat database
        3. Setting up database parameter pada proyek
        4. Testing

        modified:   README.md
        modified:   proyek/settings.py


#### 3.2 Setting up django-environ

        modified:   .gitignore
        modified:   README.md
        modified:   proyek/settings.py


### ------------------------------------------------------
### 4. DJANGO ADMIN
### ------------------------------------------------------


#### 4.1 Aktifkan django admin

        Steps:

        1. Run migrate

        modified:   README.md
        modified:   proyek/settings.py


#### 4.2 Membuat superuser

        Steps:

        1. Dari terminal ketik ini:
        > 'python manage.py createsuperuser' dan ikuti perintah yang muncul

        modified:   README.md


### ------------------------------------------------------
### 5. JALANKAN DJANGO
### ------------------------------------------------------


#### 5.1 Menjalankan django untuk kali pertama

        Steps:

        1. Jalankan lokal server => python manage.py runserver
        2. Buka browser, gunakan url ini => http://127.0.0.1:8000/

        modified:   README.md


### ------------------------------------------------------
### 6. HALLO WORLD
### ------------------------------------------------------


#### 6.1 Menampilkan Hallo World!

        Steps:

        1. Pada main/views
           1.1 Buat home_page method
           2.1 Import HttpResponse
        2. Pada main app buat urls.py file 
        3. Include urls dari main app pada urls proyek

        modified:   README.md
        new file:   apps/main/urls.py
        modified:   apps/main/views.py
        modified:   proyek/urls.py


### ------------------------------------------------------
### 7. TEMPLATE, VIEWS, URLS DAN STATIC FILES
### ------------------------------------------------------


#### 7.1 Membuat halaman home page

        Steps:

        1. Aktifkan django template
        2. Buat folder templates => templates
        3. Buat folder 'main' di dalam templates => templates/main 
        4. Buat index.html => templates/main/index.html
        5. Buat home page pada index.html
        6. Load index.html pada home_page method

        modified:   README.md
        modified:   apps/main/views.py
        modified:   proyek/settings.py
        new file:   templates/main/index.html


#### 7.2 Mengkonfigurasi static files

        Steps:

        1. Buat static folder => iklankan/static
        2. Buat file custom.css => iklankan/static/custom.css
        3. Buat konfigurasi static files pada settings.py
        4. Serving static files during development
        5. Load static files


### ------------------------------------------------------
### 8. MEMBUAT REMOTE REPOSITORY - GITHUB
### ------------------------------------------------------


#### 8.1 Modifikasi README.md file

        modified:   README.md


#### 8.2 Membuat remote repository pada Gihub dan push files ke repository

        https://github.com/gurnitha/django-iklankan


### ------------------------------------------------------
### 9. TEMPLATE DAN TEMPLATE INHERITANCE
### ------------------------------------------------------


#### 9.1 Menamabahkan html template pada home page

        Steps:

        1. Copy paste html template pada index.html
        2. Lakukan test
        3. Note: tampilannya tdk sempurna krn assets(js, css) belum ada

        modified:   README.md
        modified:   templates/main/index.html


#### 9.2 Menambahkan assets pada static files

        Steps:

        1. Tambahkan asset pada static files
        2. Load atau unggah static files pada home page
        3. Inspect hasilnya

        modified:   README.md
        new file:   static/css/flexslider.css
        ...
        new file:   static/css/font-awesome.min.css
        modified:   templates/main/index.html


#### 9.3 Menggunakan template inheritance

        Steps:

        1. Membuat base.html template
        2. Pindahkan home template ke base.html
        3. Extends base.html pada home page (index.html)
        4. Test hasilnya

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/main/index.html


#### 9.4 Mengelompokan bagian dari base template

        Steps:

        1. Load static files
        2. Membuat block tamplate tags
        3. Memindahkan kelompok kontent dari base template ke home page
        4. Test 

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/main/index.html


#### 9.5 Konklusi

        Menggunakan template dan template inheritance
        membuat pekerjaan menjadi:
        
        1. Lebih efisien.
        2. Tidak melakukan pengulangan codes karena
           pengulangan codes dapat dihindari.
        3. Hasilnya tetap sama.

        modified:   README.md


### -----------------------------------------------------------------
### 10. DJANGO MVT HOME PAGE: MODEL, VIEWS DAN TEMPLATES - SLIDER TOP
### -----------------------------------------------------------------


#### 10.1 Membuat skema model Slider

        Steps:

        1. Analisis template codes
        2. Membuat skema model/tabel Slider

        modified:   README.md
        modified:   apps/main/models.py       


#### 10.2 Migrasi

        Steps:

        1. Buka terminal dan pastikan terminal pointing proyek root
           dan virtual environmenet dalam keadaan aktif
        2. Melihat perintah yang tersedia
        3. Jalankan migrasi
        3. Lihat hasilnya

        Note:

        Migrasi adalah cara Django menyebarkan perubahan yang Anda buat 
        pada model Anda (menambahkan bidang, menghapus model, dll.) 
        ke dalam skema basis data Anda. 

        Source: https://docs.djangoproject.com/en/3.2/topics/migrations/

        modified:   README.md
        new file:   apps/main/migrations/0001_initial.py


#### 10.3 Mencatatkan model SliderTop pada admin.py

        Steps:

        1. Catatkan model SliderTop pada admin.py
        2. Lihat hasilnya

        modified:   README.md
        modified:   apps/main/admin.py


#### 10.4 Mempersiapkan data untuk SliderTop

        Steps:

        1. Ambil data dari template

        modified:   README.md


#### 10.5 Memasukan data pada tabel SliderTop di dalam database

        Steps:

        1. Ambil data 
        3. Masukan data
        2. Save
        3. Ulangi lagi step 1, 2 dan 3

        modified:   README.md


#### 10.6 Lihat hasilnya

        Steps:

        1. Buka Admin panel
        2. Buka table Slider Top 

        modified:   README.md


#### 10.7 Menampilkan data SliderTop pada home page

        Steps:

        1. Buka views.py dan import SliderTop model 
        2. Ambil semua data dari SliderTop dan tempatkan pada sebuah variabel
        3. Tempatkan variable tsb pada context
        4. Masukan context sebagai parameter dari render method 
        5. Tampilkan semua data pada Slider top di home page

        modified:   README.md
        modified:   apps/main/views.py
        modified:   templates/base.html



#### 10.8 Memindahkan background image SliderTop dari css ke template

        Steps:

        1. Pindahkan backgound image dari css ke template
        2. Non-aktifkan url image pada css
        2. Periksa hasilnya di browser



#### 10.9 (TIDAK BERHSIL) Membuat background image SliderTop dinamis

        Steps:

        1. Tambahkan image field pada SliderTop model
        2. Install Pillow
        3. Jalankan migrasi
        4. Buat path untuk image
        5. Masukan data image pada tabel di database
        6. Menampilkan image dari database pada slider

        NOTE:

        1. Berhasil tapi tidak sempurna.
        2. Diputuskan untuk kembali ke posisi 10.7

        modified:   README.md
        new file:   apps/main/migrations/0002_slidertop_image.py
        new file:   apps/main/migrations/0003_alter_slidertop_image.py
        modified:   apps/main/models.py
        modified:   apps/main/views.py
        new file:   media/slider-top/images/SushantSinghRajput.PNG
        new file:   media/slider-top/images/art.jpg
        new file:   media/slider-top/images/art_6G88H5r.jpg
        new file:   media/slider-top/images/art_FNJUtKd.jpg
        new file:   media/slider-top/images/art_HddeWtO.jpg
        new file:   media/slider-top/images/art_p8rpjk8.jpg
        new file:   media/slider-top/images/art_tjebAhM.jpg
        new file:   media/slider-top/images/banner.jpg
        new file:   media/slider-top/images/contact01.PNG
        new file:   media/slider-top/images/contact01_94WbuNs.PNG
        new file:   media/slider-top/images/contact02.PNG
        modified:   proyek/settings.py
        modified:   proyek/urls.py
        modified:   templates/base.html


#### 10.10 Modifikasi README.md

        modified:   README.md


#### 10.11 Memindahkan Slider Top dari base template ke home page

        Steps:

        1. Copy slider component dari base template
        2. Paste slider component pada index.html
        3. Hapus slider component dari base template
        4. Test

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/main/index.html


#### 10.12 Membenahi tata letak codes

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/main/index.html


### -----------------------------------------------------------------
### 11. DJANGO MVT HOME PAGE: CATEGORI
### -----------------------------------------------------------------


#### 11.1 Membuat Kategori model, migrasi, admin dan mengisi data

        Steps:

        1. Membuat analisa code
        2. Membuat dumi data kategori hasil analisis
        3. Membuat Kategori model
        4. Menjalankan migrasi dan lihat hasilnya pd db
        5. Mencatatan Kategori model pada admin dan
           lihat hasilnya pada Admin panel
        6. Menambahkan slug field pada Kategori model
           -jalankan migrasi
        7. Membuat slug field terisi secara otomatis
        8. Memasukan data pada tabel Kategori

        modified:   README.md
        modified:   apps/main/admin.py
        new file:   apps/main/migrations/0004_kategori.py
        new file:   apps/main/migrations/0005_kategori_slug.py
        modified:   apps/main/models.py



#### 11.2 Memanggil dan mendisplay data Kategori dari database pada home page

        Steps:

        1. Mingimpor Kategori model
        2. Memanggil semua data dari Kategori tabel
        3. Menempatkannya pada context
        4. Mendisplay data Kategori pada Kategori di home page
        5. Hasilnya
        
        modified:   apps/main/views.py
        modified:   templates/main/index.html


### -----------------------------------------------------------------
### 12. DJANGO MVT HOME PAGE: IKLAN TERPOPULER
### -----------------------------------------------------------------


#### 12.1 Membuat Iklan model, migrasi, admin dan mengisi data

        Steps:

        1. Membuat analisa code
        2. Membuat dumi data Iklan hasil analisis
        3. Membuat Iklan model
        4. Menjalankan migrasi dan lihat hasilnya pd db
        5. Mencatatan Iklan model pada admin dan
           lihat hasilnya pada Admin panel
        6. Menambahkan field deskripsi_singkat pada Iklan model
        7. Memasukan data pada tabel Iklan

        modified:   README.md
        modified:   apps/main/admin.py
        new file:   apps/main/migrations/0006_iklan.py
        new file:   apps/main/migrations/0007_iklan_deskripsi_singkat.py
        modified:   apps/main/models.py
        new file:   media/iklan/images/ad1.jpg
        new file:   media/iklan/images/ad2.jpg
        new file:   media/iklan/images/ad4.jpg
        new file:   media/iklan/images/ad5.jpg
        new file:   media/iklan/images/cat11.png
        new file:   media/iklan/images/client_1.jpg


#### 12.2 Menambahkan klasifikasi iklan field pada Iklan model

        Steps:

        1. Buat KLASIFIKASI_IKLAN
        2. Buat klasifikasi field menggunakan pilihan KLASIFIKASI_IKLAN
        2. Jalankan migrasi

        modified:   README.md
        new file:   apps/main/migrations/0008_iklan_klasifikasi.py
        modified:   apps/main/models.py


#### 12.3 Menampilkan data Iklan terpopular pada home page

        Steps:

        1. Mengimpor model Iklan 
        2. Memanggil data iklan dgn klasisifkai terpopular 
           dan tempatkan mereka pada varibel iklan_terpopuler
        3. Tambahkan ke dalam context
        4. Tampilkan data pada blok Iklan Terpopular pada home page
        5. Lihat hasilnya

        modified:   README.md
        modified:   apps/main/views.py
        new file:   media/iklan/images/ad3.jpg
        new file:   media/iklan/images/art.jpg
        modified:   templates/main/index.html