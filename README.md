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


#### 1.7 Membuat model data blog

        :: Aktivitas:

        1. Modifikasi file README.md


#### 1.7.1 Membuat model data blog - Part 1: Membuat model Post

        :: Aktivitas:

        1. Membuat model Post

        modified:   01_blog/blog/models.py

        :: Daftar file yang berubah:

        modified:   01_blog/blog/models.py
        modified:   README.md


#### 1.7.2 Membuat model data blog - Part 2: Menambahkan kolom datetime

        :: Aktivitas:

        1. Menambahkan kolom datetime pada model Post

        modified:   01_blog/blog/models.py

        :: Daftar file yang berubah:

        modified:   01_blog/blog/models.py
        modified:   README.md


#### 1.7.3 Membuat model data blog - Part 3: Menentukan urutan sortir default

        :: Aktivitas:

        1. Menentukan urutan sortir default

        modified:   01_blog/blog/models.py

        :: Daftar file yang berubah:

        modified:   01_blog/blog/models.py
        modified:   README.md
        modified:   README.md


#### 1.7.4 Membuat model data blog - Part 4: Menambahkan indeks basis data

        :: Aktivitas:

        1. Menentukan urutan sortir default

        modified:   01_blog/blog/models.py

        :: Daftar file yang berubah:

        modified:   01_blog/blog/models.py
        modified:   README.md


#### 1.7.4 Membuat model data blog - Part 4: Menambahkan indeks basis data

        :: Aktivitas:

        1. Menentukan urutan sortir default

        modified:   01_blog/blog/models.py

        :: Daftar file yang berubah:

        modified:   01_blog/blog/models.py
        modified:   README.md


#### 1.7.5 Membuat model data blog - Part 5: Menambahkan bidang status

        :: Aktivitas:

        1. Menentukan urutan sortir default

        modified:   01_blog/blog/models.py

        :: Daftar file yang berubah:

        modified:   01_blog/blog/models.py
        modified:   README.md


#### 1.7.6 Membuat model data blog - Part 6: Mengaktifkan aplikasi

        :: Aktivitas:

        1. Menambahkan aplikasi blog pada mysite/settings.py
        modified:   01_blog/mysite/settings.py

        2. Menjalankan migrasi
        new file:   01_blog/blog/migrations/0001_initial.py

        :: Daftar file yang berubah:

        new file:   01_blog/blog/migrations/0001_initial.py
        modified:   01_blog/mysite/settings.py
        modified:   README.md

        NOTE:

        :: Evaluating enumeration class Status:

        # :: Import Post model from blog
        >>> from blog.models import Post

        # :: Checking value-label pairs in sub class Status
        >>> Post.Status.choices
        [('DF', 'Draft'), ('PB', 'Published')]        

        # :: Checking Status's lebels
        >>> Post.Status.labels
        ['Draft', 'Published']

        # :: Checking Status's values
        >>> Post.Status.values
        ['DF', 'PB']

        # :: Checking Status's names
        >>> Post.Status.names
        ['DRAFT', 'PUBLISHED']


#### 1.7.7 Membuat model data blog - Part 7: Menambahkan many-to-one hubungan

        :: Aktivitas:

        1. Menambahkan kolom author pada Post model
        modified:   01_blog/blog/models.py

        :: Daftar file yang berubah:

        modified:   01_blog/blog/models.py
        modified:   README.md


#### 1.7.8 Membuat model data blog - Part 8: Membuat dan menerapkan migrasi

        :: Aktivitas:

        1. Membuat migratsi
        > python manage.py makemigrations blog
        Migrations for 'blog':
          blog\migrations\0001_initial.py
            - Create model Post

        2. Memeriksi hasil migrasi
        > python manage.py sqlmigrate blog 0001

        BEGIN;
        --
        -- Create model Post
        --
        CREATE TABLE "blog_post" (
                "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
                "title" varchar(250) NOT NULL, 
                "slug" varchar(250) NOT NULL, 
                "body" text NOT NULL, 
                "publish" datetime NOT NULL, "created" datetime NOT NULL, 
                "updated" datetime NOT NULL, "status" varchar(2) NOT NULL, 
                "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);

        CREATE INDEX "blog_post_slug_b95473f2" ON "blog_post" ("slug");
        CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
        CREATE INDEX "blog_post_publish_bb7600_idx" ON "blog_post" ("publish" DESC);
        COMMIT;

        3. Menerapkan migrasi
        > python manage.py migrate blog 0001


        :: Daftar file yang berubah:

        modified:   01_blog/blog/migrations/0001_initial.py
        modified:   README.md


#### 1.8. Membuat situs administrasi untuk model