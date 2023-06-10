# DJANGO 4 BY EXAMPLE
Belajar Framework Django dari Buku DJANGO 4 BY EXAMPLE karangan Antonio Mele

Github: https://github.com/gurnitha/django-4-by-example


## 0. SETUP

#### 01.1 Memodifikasi file README.md

        :: Aktivitas:

        1. Membuat repositori pada Github
        2. Meng-clone repositori dari Github
        3. Memodifikasi file .gitignore
        4. Memodifikasi file README.md

        :: Daftar file yang berubah:

        modified:   .gitignore
        modified:   README.md


## 1. MEMBUAT APLIKASI BLOG

        :: Aktivitas:

        1. Memodifikasi file README.md

        :: Daftar file yang berubah:

        modified:   README.md


#### 1.1 Membuat Python virtual environment

        :: Aktivitas:

        1. Memeriksa versi python, pip dan virtualenv

        > python --version
        > pip --version
        > virtualenv --version

        2. Membuat virtual environment dengan nama venv3942

        > python -m venv venv3942

        :: Daftar file yang berubah:

        modified:   README.md

        NOTE:

        venv3942 tidak dicatat di dalam git karena
        dalam .gitignore file telah dibuat perintah
        agar venv3942 tidak dicatat dalam git.


#### 1.2 Menginstal Django versi 4.2

        :: Aktivitas:

        1. Mengaktifkan venv3942
        > venv3942\Scripts\activate
        (venv3942) hp@ING:Django4ByExample ~

        2. Menginstal django versi 4.2

        (venv3942) hp@ING:Django4ByExample ~
        > pip install django==4.2.*

        3. Memeriksa file yang terinstall
        > pip list

        4. Membuat requirements.txt file
        > pip freeze > requirements.txt

        :: Daftar file yang berubah:

        modified:   README.md
        new file:   requirements.txt


#### 1.3 Memembuat Proyek Pertama Django

        :: Aktivitas:

        1. Mengaktifkan venv3942
        > venv3942\Scripts\activate
        (venv3942) hp@ING:Django4ByExample ~

        2. Membuat proyek django
        > django-admin startproject mysite .

        :: Daftar file yang berubah:

        new file:   01_blog/manage.py
        new file:   01_blog/mysite/__init__.py
        new file:   01_blog/mysite/asgi.py
        new file:   01_blog/mysite/settings.py
        new file:   01_blog/mysite/urls.py
        new file:   01_blog/mysite/wsgi.py
        modified:   README.md

        :: NOTE

        Sukses membuat proyek django pertama :)


#### 1.4 Menerapkan migrasi database awal

        :: Aktivitas:

        1. Menjalankan perintah migrasi
        
        (venv3942) hp@ING:Django4ByExample ~
        > python manage.py makemigrations
        >  python manage.py migrate

        :: Daftar file yang berubah:

        modified:   README.md

        :: NOTE

        Sukses menjalankan migrasi :)


#### 1.5 Menjalankan lokal server 

        :: Aktivitas:

        1. Menjalankan lokal server
        
        (venv3942) hp@ING:Django4ByExample ~
        > python manage.py runserver

        2. Melihat tampilan proyek pada browser

        http://127.0.0.1:8000/


        :: Daftar file yang berubah:

        modified:   README.md

        :: NOTE

        Django proyek suskses dijalankan :)


#### 1.6 Membuat aplikasi

        :: Aktivitas:

        1. Membuat aplikasi
        
        (venv3942) hp@ING:Django4ByExample ~
        > python manage.py startapp blog

        :: Daftar file yang berubah:

        new file:   01_blog/blog/__init__.py
        new file:   01_blog/blog/admin.py
        new file:   01_blog/blog/apps.py
        new file:   01_blog/blog/migrations/__init__.py
        new file:   01_blog/blog/models.py
        new file:   01_blog/blog/tests.py
        new file:   01_blog/blog/views.py
        modified:   README.md

        :: NOTE

        Sukses membuat aplikasi baru :)



