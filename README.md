# django-kamu-bisa-apa
Membuat aplikasi sebagai wadah untuk orang2 Indonesia yang kreatif 


### 1. INISIAL KOMIT
### ---------------------------------------------------------------


### 1.1 Membuat remote repositori di Github



### 2. DJANGO PROJECT DAN APP
### ---------------------------------------------------------------


### 2.1 Membuat django project 'core' dan django app 'apps/profiles'

        modified:   README.md
        new file:   apps/profiles/__init__.py
        new file:   apps/profiles/admin.py
        new file:   apps/profiles/apps.py
        new file:   apps/profiles/migrations/__init__.py
        new file:   apps/profiles/models.py
        new file:   apps/profiles/tests.py
        new file:   apps/profiles/views.py
        new file:   core/__init__.py
        new file:   core/asgi.py
        new file:   core/settings.py
        new file:   core/urls.py
        new file:   core/wsgi.py
        new file:   manage.py



### 3. MEMBUAT HALAMAN profile_list dan profile_detail
### ---------------------------------------------------------------


#### 3.1 Membuat halaman profile_list

        modified:   README.md
        new file:   apps/profiles/templates/profiles/profile_list.html
        new file:   apps/profiles/urls.py
        modified:   apps/profiles/views.py
        modified:   core/urls.py


#### 3.2 Membuat halaman profile_detail

        modified:   README.md
        new file:   apps/profiles/templates/profiles/profile_detail.html
        modified:   apps/profiles/urls.py
        modified:   apps/profiles/views.py


#### 3.3 Menghubungkan halaman profile_list dan profile_detail

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_detail.html
        modified:   apps/profiles/templates/profiles/profile_list.html
        modified:   apps/profiles/urls.py
        modified:   apps/profiles/views.py



### 4. TEMPLATES DAN STATIC FILES
### ---------------------------------------------------------------


#### 4.1 Menambahkan template theme pada halaman profile_list dan profile_detail

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_detail.html
        modified:   apps/profiles/templates/profiles/profile_list.html


#### 4.2 Menambahkan dan mengunggah static files

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_detail.html
        modified:   apps/profiles/templates/profiles/profile_list.html
        modified:   core/settings.py
        modified:   core/urls.py
        ...
        new file:   static/assets/images/DevSearch Projects.jpg
        new file:   static/assets/images/Devsearch Home.jpg


#### 4.3 Template inheritance and include

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_detail.html
        modified:   apps/profiles/templates/profiles/profile_list.html
        modified:   core/settings.py
        new file:   templates/base.html
        new file:   templates/shared/header.html


#### 4.4 Modifikasi halaman profile_list

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_list.html

        
### 5. MODELS UNTUK PROFILES
### ---------------------------------------------------------------


#### 5.1 Membuat model Profil and Skill, migrasi dan register model pada admin

        modified:   README.md
        modified:   apps/profiles/admin.py
        new file:   apps/profiles/migrations/0001_initial.py
        new file:   apps/profiles/migrations/0002_auto_20211022_2118.py
        modified:   apps/profiles/models.py
        new file:   profiles/ing.PNG
        new file:   static/profiles/user-default.png
