# LAB-AP-1-2026

## 📚 Repositori Tugas Praktikum Algoritma & Pemrograman 2026

Selamat datang di repositori resmi **Praktikum Algoritma & Pemrograman 2026**. Repositori ini digunakan oleh mahasiswa untuk mengumpulkan seluruh Tugas Praktikum (TP) selama semester berlangsung melalui mekanisme *Fork* dan *Pull Request* (PR) di GitHub.

---

## 🛠️ Prasyarat (Requirements)

Sebelum memulai, pastikan Anda telah menyiapkan hal-hal berikut:
1. **Akun GitHub**: Terdaftar di [github.com](https://github.com/).
2. **Git CLI**: Terinstal di komputer Anda ([Download Git](https://git-scm.com/)). Cek instalasi via terminal:
   ```bash
   git --version
   ```
3. **Text Editor / IDE**: Visual Studio Code, PyCharm, atau editor lain pilihan Anda.

---

## 📁 Struktur Repositori & Penamaan File

Seluruh folder mahasiswa (`NIM`) dan subfolder praktikum (`Praktikum-1` s.d. `Praktikum-9`) **telah disediakan di repositori ini**.

### Visualisasi Struktur Folder:
```text
LAB-AP-1-2026/
├── H071261041/
│   ├── Praktikum-1/
│   │   ├── TP1_1_H071261041.py
│   │   └── TP1_2_H071261041.py
│   ├── Praktikum-2/
│   │   └── TP2_1_H071261041.py
│   ├── ...
│   └── Praktikum-9/
├── H071261042/
└── README.md
```

### Aturan Penamaan File & Folder:
| Elemen | Format / Aturan Penamaan | Contoh | Status |
| :--- | :--- | :--- | :--- |
| **Folder Mahasiswa** | `<NIM>` *(Tanpa spasi/nama)* | `H071261041` | *Sudah tersedia* |
| **Folder Praktikum** | `Praktikum-<n>` *(n = 1 s.d. 9)* | `Praktikum-1`, `Praktikum-2` | *Sudah tersedia* |
| **File Tugas** | `TP<n>_<noSoal>_<NIM>.py` | `TP1_1_H071261041.py`, `TP2_3_H071261041.py` | *Dibuat oleh Mahasiswa* |

---

## 🚀 Alur Pengumpulan Tugas (Step-by-Step Tutorial)

Ikuti langkah-langkah berikut secara berurutan:

### 1. Fork Repositori (Sekali di Awal Semester)
1. Buka halaman repositori utama **LAB-AP-1-2026** di GitHub.
2. Klik tombol **Fork** di pojok kanan atas halaman.
3. Klik **Create fork** untuk menyalin repositori ini ke akun GitHub Anda.

---

### 2. Clone Repositori Fork ke Komputer
Buka Terminal / Command Prompt / Git Bash di komputer Anda, lalu jalankan perintah:

```bash
git clone https://github.com/USERNAME_ANDA/LAB-AP-1-2026.git
cd LAB-AP-1-2026
```
> [!IMPORTANT]
> Ganti `USERNAME_ANDA` dengan username akun GitHub Anda sendiri.

---

### 3. Sync Fork & Pull Terbaru (Sebelum Mengerjakan Praktikum Baru)
Setiap akan mengerjakan praktikum baru, pastikan repositori fork dan komputer Anda sudah menerima struktur folder terbaru dari repo utama:
1. Di web GitHub repositori fork Anda, klik **Sync fork** $\rightarrow$ **Update branch**.
2. Di terminal komputer Anda, jalankan:
   ```bash
   git checkout main
   git pull origin main
   ```

---

### 4. Buat dan Pindah ke Branch Praktikum (`praktikum-n`)
Selalu kerjakan tugas pada **branch baru** (bukan langsung di branch `main`):

```bash
# Contoh untuk Praktikum 2:
git checkout -b praktikum-2
```

---

### 5. Masuk ke Folder Praktikum Yang Sesuai
Navigasikan ke folder NIM Anda, lalu masuk ke folder praktikum minggu ini:

```bash
# Contoh untuk mahasiswa NIM H071261041 pada Praktikum 2:
cd H071261041/Praktikum-2
```

---

### 6. Simpan File Tugas Anda
Simpan seluruh file program Python Anda di dalam folder `Praktikum-n` tersebut dengan format penamaan:
`TP<n>_<noSoal>_<NIM>.py`

*Contoh:*
- File soal 1: `TP2_1_H071261041.py`
- File soal 2: `TP2_2_H071261041.py`

---

### 7. Stage (Add) dan Commit Perubahan
Setelah menyelesaikan kode program:

1. **Cek Status Perubahan:**
   ```bash
   git status
   ```

2. **Tambahkan File ke Staging Area:**
   ```bash
   git add TP2_1_H071261041.py
   # Atau tambahkan seluruh file di folder Praktikum saat ini:
   git add .
   ```

3. **Lakukan Commit dengan Pesan Deskriptif:**
   ```bash
   git commit -m "Menambahkan tugas TP2 no 1 dan 2 H071261041"
   ```

---

### 8. Push Branch ke Repositori Fork Anda
Unggah branch tugas dari komputer ke akun GitHub Anda:

```bash
git push origin praktikum-2
```

---

### 9. Buat Pull Request (PR) di GitHub
1. Buka repositori hasil **fork** Anda di halaman browser GitHub.
2. Klik tombol **Compare & pull request** yang muncul.
3. Pastikan perbandingan branch:
   - **base repository**: `ShinZeleo/LAB-AP-1-2026` (base: `main`)
   - **head repository**: `USERNAME_ANDA/LAB-AP-1-2026` (compare: `praktikum-2`)
4. Berikan judul Pull Request yang jelas, contoh: `[TP-2] H071261041`.
5. Klik **Create pull request**.

---

## 🔑 Autentikasi Push di GitHub (Personal Access Token / PAT)

Jika saat melakukan `git push` Anda diminta memasukkan Password, gunakan **Personal Access Token (PAT)**:
1. Profile > **Settings** > **Developer settings** > **Personal access tokens** > **Tokens (classic)**.
2. Klik **Generate new token (classic)**, isi note, centang scope **`repo`**, lalu **Generate token**.
3. Gunakan token ini sebagai *Password* di terminal/Git.

---

## 💡 Tips & Troubleshooting

- **Cek Branch Aktif**: Ketik `git branch` untuk melihat branch yang sedang aktif sebelum mulai mengedit file.
- **Sync Fork**: Selalu lakukan **Sync Fork** di GitHub sebelum membuat branch baru agar folder terbaru terunduh.
