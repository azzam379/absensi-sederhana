# Pemenuhan Unit Kompetensi Skema Junior Programming (JP)

Dokumen ini menjelaskan bagaimana proyek rekayasa perangkat lunak **Sistem Absensi Sederhana** yang telah dibangun dan di-_deploy_ ke Vercel Architecture dan Neon Database ini memenuhi **10 kriteria utama** dalam Uji Kompetensi Keahlian (UJK) Skema Junior Programming.

---

## 1. Menggunakan Struktur Data
Sistem menggunakan tipe struktur data yang variatif dan kokoh seperti pengolahan *List/Array* dan struktur hierarki *Dictionary/Object* di Python. Pada bagian API (FastAPI) dan Frontend (JavaScript), arus data dari *Database* ditangkap, diolah/dipecah, dan di-parsing (*Serialization/Deserialization*) ke dalam objek agar dapat menetas sempurna menjadi baris-baris pada tabel penampil (HTML).

## 2. Menerapkan Perintah Eksekusi
*Output* aplikasi berhasil dieksekusi bolak-balik.(*Full duplex*). Data riwayat kehadiran yang melayang dari peladen (*Server Cloud* Vercel) ditangkap dan dieksekusi nyata ke *browser* pengguna dengan cara memanipulasi _Document Object Model_ (DOM) Web melalui interaksi fungsi JavaScript secara berkelanjutan.

## 3. Reusable Subrutin
Logika API dirancang ulang dan dibungkus menjadi fungsi-fungsi modular yang bisa digunakan berkali-kali tanpa teknik penyalinan manual (*DRY: Don't Repeat Yourself*). Contoh konkritnya adalah fungsi utilitas koneksi `get_db()` yang disuntikkan terus-menerus ke tiap penembakan spesifik di FastAPI (melalui fitur pendamping `Depends`), maupun pada file utilitas *Frontend* `api.js` (Fungsi general `api.post` dan `api.get`).

## 4. Pemrograman Terstruktur
Bentuk aplikasi tidak ditumpuk menjadi naskah 1 file raksasa (monolitik), melainkan mematuhi standar *Separation of Concern*. Mulai dari memisahkan total lapisan Visual/Klien (`/frontend`) dan lapisan logika Peladen (`/api`). Menukik pada ranah Backend-nya pun, alur dipecah rapi secara modular: Pemetaan Rute (`routers/`), Penghubung Database (`database.py`), Definisi Model Entitas (`models.py`), serta Skema Validasi (`schemas.py`). 

## 5. Menggunakan Library
Integrasi ini secara krusial melibatkan pustaka / *packages* modern tervalidasi global:
- **`fastapi`** dan **`uvicorn`** (Pondasi Web Service)
- **`sqlalchemy`** (Penerjemah Objek-Relasional SQL)
- **`pydantic`** (Benteng Validasi Struktur Data ketat)
- **`pytest`** (Pisau bedah Unit Testing)

## 6. Menggunakan SQL
Kendati menghindari tulisan skrip SQL murni (yang dianggap rawan bocor/*Injection* di era kini), aplikasi tetap menjaga kepatuhan kaidah DML/DDL ketat dari SQL secara transparan berbasis **ORM (Object-Relational Mapping)**. Perintah inisiasi standar `SELECT, INSERT, UPDATE, DELETE` diterjemahkan cermat ke dalam tata bahasa SQLAlchemy yang jauh lebih bersih via PostgreSQL bawaan (contoh: `db.query(models.Siswa).add(...)`).

## 7. Menerapkan Akses Basis Data
Meningkatkan tantangan dari pedoman awal (melawan ketergantungan SQLite luring), aplikasi ini dipresentasikan memakai jalur transmisi internet langsung. Koneksi basis daya tersambung lintas benua mencapai awan **Neon.tech PostgreSQL**, mengatasi  *file serverless*. Semua diverifikasi  menggunakan konfigurasi deteksi *Remote URL String* standar di `database.py`.

## 8. Mengimplementasikan Algoritma
Logika pemfilteran diterapkan pada algoritma asinkron pengunduhan tabel rekapitulasi harian. Seluruh interaksi rekam data juga difilter oleh pintu logika IF-ELSE (permasalahan Foreign Key Check): Sebelum merestui perintah input kehadiran absensi, algoritma Backend secara proaktif memeriksa eksistensi fisik Nomor ID sang Siswa—menolak keras proses jika Siswa terbukti fiktif, menyuguhkan integritas basis data yang absolut.

## 9. Melakukan Debugging
Aplikasi melewati proses intervensi kesalahan *debugging* yang solid selama mode perancangan berfase. Kasus penolakan komunikasi lintas sumber (*CORS Temporary 307 Redirects*) ketika ketiadaan simbol *Trailing Slash* garis miring `/` di ujung *URL* rute Frontend, hingga kasus deteksi galat tersembunyi `BOM UTF-16 Encoding` karena *incompatibility log* peranti bawaan PowerShell sukses dipersempit dan dideteksi murni (Analisis Bug-Fix).

## 10. Pengujian Unit Program
Aplikasi diperkuat fondasinya memakai uji validitas tersimulasi komputer—bukan penguji manual. Lewat naskah redeem kode di bilik `api/tests/`, mesin uji otomatisasi (`pytest`) menyewa simulasi memori fana untuk menguji respon fungsi, mulai dari "Kemampuan Menambahkan Siswa secara Logika (Response: 200)" hingga "Pengujian Sengaja Salah ID Fiktif (Response: Must be a Pure 404 Warning Defect)". Bukti Kelulusan Tuntas Test: **100% Passed**.
