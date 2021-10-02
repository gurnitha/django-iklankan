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