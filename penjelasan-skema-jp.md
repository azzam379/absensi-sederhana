# Pemenuhan Unit Kompetensi Skema Junior Programming (JP)

Dokumen ini menjelaskan bagaimana proyek rekayasa perangkat lunak **Sistem Absensi Sederhana** yang telah dibangun dan di-_deploy_ ke Vercel Architecture dan Neon Database ini memenuhi **10 kriteria utama** dalam Uji Kompetensi Keahlian (UJK) Skema Junior Programming.

---

## 1. Menggunakan Struktur Data
Sistem menggunakan tipe struktur data hierarki seperti *Dictionary/Object* dan struktur jamak (*Array/List*). Pada Python, kita memakai bentukan *Class Object* Pydantic untuk memvalidasi struktur data secara statis.
*   **Contoh & Lokasi File:**
    *   `api/schemas.py`: Terdapat struktur data berbasis kelas (`class SiswaCreate(BaseModel)`) untuk merekam skema/tipe teks murid.
    *   `frontend/js/siswa.js`: Variabel `const data = await api.get('/api/siswa/');` menangkap respons *Array of Objects* dari database yang siap diolah menjadi elemen UI di DOM.

## 2. Menerapkan Perintah Eksekusi
*Output* aplikasi berhasil dieksekusi bolak-balik.(*Full duplex*). Data riwayat kehadiran yang melayang dari peladen dieksekusi secara beruntun (*Event-driven*) dengan cara memanipulasi _Document Object Model_ (DOM) antarmuka Web.
*   **Contoh & Lokasi File:**
    *   `frontend/index.html`: Perintah eksekusi dipicu menggunakan event `<button onclick="tambahSiswa()">` dan event deteksi pergerakan `document.addEventListener('DOMContentLoaded', ...)` yang memanggil kode Javascript untuk memuat data tanpa refresh (*Async*).

## 3. Reusable Subrutin
Logika API dirancang ulang dan dibungkus menjadi fungsi-fungsi modular (Subrutin) yang bisa dipanggil ratusan kali tanpa menulis ulang (*DRY: Don't Repeat Yourself*).
*   **Contoh & Lokasi File:**
    *   `api/database.py`: Fungsi utilitas `def get_db():` disuntikkan terus-menerus menggunakan injektor `Depends()` di hampir seluruh operasi CRUD FastAPI.
    *   `frontend/js/api.js`: Obyek `const api = { ... }` menyatukan *subroutine* `get`, `post`, `put`, dan `delete` yang secara modular dipinjam/dieksekusi ulang berkali-kali oleh file `siswa.js` dan `absensi.js`.

## 4. Pemrograman Terstruktur
Arsitektur aplikasi dipecah rapi secara modular/hierarki agar tidak menjadi satu naskah raksasa (monolitik). Pemisahan total terlihat antara *Presentation Layer* (Layar Interaksi Pengguna) dan *Business Logic* (Sistem Otak API).
*   **Contoh & Lokasi File/Direktori:**
    *   Direktori `/frontend/` khusus memuat visual dan logika klien statis (HTML/CSS/JS).
    *   Direktori `/api/` dikhususkan menampung mesin. Didalamnya masih dipecah secara berstruktur: `api/routers/` (untuk rute alamat web), `api/models.py` (untuk pemetaan tabel), dan `api/database.py` (spesial untuk koneksi).

## 5. Menggunakan Library
Alih-alih menulis sintaks dasar (seperti membangun *web server HTTP* dari titik nol), integrasi ini meminjam *packages* luar tervalidasi global.
*   **Contoh & Lokasi File:**
    *   `requirements.txt`: Memuat seluruh dependensi krusial (Library Python) seperti `fastapi`, `uvicorn`, `sqlalchemy`, dan `psycopg2-binary`.
    *   `api/main.py`: Penggunaan pustaka ditandai dari baris awalan seperti `from fastapi import FastAPI`.

## 6. Menggunakan SQL
Kendati menghindari tulisan skrip SQL berformat "mentah" untuk keamanan, aplikasi tetap menjalankan DML/DDL standar SQL menggunakan teknik abstraksi **ORM (Object-Relational Mapping)**.
*   **Contoh & Lokasi File:**
    *   `api/routers/siswa.py`: Sintaks `db.query(models.Siswa).all()` mewakili eksekusi *query* `SELECT * FROM siswa`. Sedang sintaks `db.add(db_siswa)` dan `db.commit()` mewakili kaidah *query* `INSERT INTO siswa ...`.

## 7. Menerapkan Akses Basis Data
Meningkatkan level keamanan dan stabilitas dari format *file* lokal murni menjadi layanan komputasi awan. Server menjalin pertukaran paket data rahasia dengan PostgreSQL Cloud.
*   **Contoh & Lokasi File:**
    *   `api/database.py`: Proses akses (*Database Connection String*) difasilitasi di baris `SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:***@ep-***.aws.neon.tech/neondb..."`.

## 8. Mengimplementasikan Algoritma
Logika perlindungan Data dan alur prosedural diterapkan agar alur sistem tidak salah alamat (Misal, menginput kehadiran untuk ID Siswa yang tidak pernah bersekolah).
*   **Contoh & Lokasi File:**
    *   `api/routers/absensi.py`: Di dalam `def create_absensi(...)`, diletakkan Algoritma Percabangan Logis (IF-ELSE) pada baris kode `if not siswa:` yang melempar *Error 404* sebelum eksekusi penyimpanan (*Foreign Key Consistency Check Algorithm*).

## 9. Melakukan Debugging
Aplikasi melewati proses intervensi pencarian galat (*Error*) komprehensif, khususnya memecahkan rintangan *serverless computing* dan keamanan lintas jalur sumber daya (*CORS*).
*   **Contoh & Lokasi File:**
    *   `vercel.json`: Debugging *CORS Temporary Redirects* diselesaikan dengan perumusan *Rewrites Rules* di berkas JSON agar semua jalur `/api/*` ter-alih rute (*Routing fix*) langsung menuju `api/main.py`.
    *   `frontend/js/api.js`: Penambahan konstanta analitik `IS_LOCAL` yang mampu mengidentifikasi dan berpindah *URL Base* secara mandiri, mengantisipasi kesalahan *fetch* ketika *hostname* bukan dari Vercel Cloud.

## 10. Pengujian Unit Program
Aplikasi tidak ditetes kualifikasinya secara manual asal raba, melainkan memiliki berkas *test runner* resmi dengan metodologi otomasi.
*   **Contoh & Lokasi File/Direktori:**
    *   Direktori `/api/tests/`: Terdapat file otomasi uji `test_siswa.py` dan `test_absensi.py` menggunakan perpustakaan Python `Pytest`.
    *   Contohnya pada fungsi `test_siswa_tidak_ditemukan()`, skrip diprogram untuk dengan sengaja menyuntik data Siswa fiktif (ID: 999), kemudian disesuaikan ekspektasinya (*assertion*) bahwa Server Python diwajibkan untuk menolak pengujian cacat tersebut (Wajib berekasi dengan *Status Code 404*).
*   **Langkah Demonstrasi Pengetesan (Via Terminal):**
    1. Buka Terminal/PowerShell dan pastikan Anda berada di direktori utama `absensi-sederhana`.
    2. Ketikkan perintah pengujian: `python -m pytest api/tests/ -v` lalu tekan Enter.
    3. Komputer akan melakukan simulasi otomatis. Jika mesin mencetak tulisan berwarna hijau **"100% PASSED"**, itu merupakan bukti konkret (hitam di atas putih) bahwa unit fungsional kode Anda telah terverifikasi aman.
