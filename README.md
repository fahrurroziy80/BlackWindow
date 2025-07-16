# 🕷️ BlackWidow – Framework OSINT Modern

“Karena intelijen seharusnya mematikan dan elegan.”

## Deskripsi Singkat
BlackWidow adalah framework reconnaissance (pengintaian) berbasis Python yang dirancang untuk penetration tester, red teamer, bug hunter, dan profesional keamanan siber. Alat ini menggunakan teknik OSINT modern untuk mengumpulkan informasi dari domain target dengan pendekatan pasif dan aktif, serta dilengkapi dengan fitur-fitur AI-assisted, notifikasi otomatis, dan kemampuan eksport laporan siap pakai.

## Fitur Utama
- **Dork Engine Pintar:** Menghasilkan dork Google/Bing otomatis untuk pencarian sensitif.
- **Pendeteksi Pola Email:** Mengumpulkan email publik dan menginferensi pola (misalnya, first.last@domain).
- **Subdomain Enumerator:** Enumerasi pasif + brute-force opsional (CRT.sh, Anubis API, DNS hit).
- **Leak Scanner:** Mendeteksi bocoran di Pastebin dan GitHub berdasarkan domain
- **Mode Pasif & Aktif:** Memilih mode hanya-pasif atau aktif (probe DNS) untuk stealth & efisiensi.

## Cara Install
1. Clone Repositori:
   ```bash
   git clone https://github.com/kali-gpt/blackwidow.git
   cd blackwidow

# Cara menggunakan
1. basic recon
   ```bash
   python3 blackwidow.py -d contoh.com
2. Mode Aktif (aktifkan brute-force DNS)
   ```bash
   python3 blackwidow.py -d contoh.com --passive False
