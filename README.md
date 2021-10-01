### MEMBUAT APLIKASI DENGAN NAMA 'IKLANKAN' MENGGUNAKAN DJANGO FRAMEWORK VERSI 3.2


### -------------------------------------------------------------------------------
### 1. INISIAL SETUP
### -------------------------------------------------------------------------------


#### 1.1 Menginstall Python, membuat proyek direktori, README.md, .gitignore file dan lokal repository

        new file:   .gitignore
        new file:   README.md


### -------------------------------------------------------------------------------
### 2. MEMBUAT DJANGO PROYEK DAN APP
### -------------------------------------------------------------------------------


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


### -------------------------------------------------------------------------------
### 3. MEMBUAT DATABASE DGN MANGGUNAKAN MYSQL
### -------------------------------------------------------------------------------


#### 3.1 Membuat database

        Steps:

        1. Mengistall 'mysqlclient' package
        2. Membuat database
        3. Setting up database parameter pada proyek
        4. Testing

        modified:   README.md
        modified:   proyek/settings.py





