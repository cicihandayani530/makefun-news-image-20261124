# THE ORRERY — NI24 Wave 1 · Akun 3 (@cicihandayani)

[![make.fun bounty](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
![rank](https://make.fun/badge/news-image-20261124/cicihandayani530/makefun-news-image-20261124/rank.svg)
![reward](https://make.fun/badge/news-image-20261124/cicihandayani530/makefun-news-image-20261124/reward.svg)

Bounty page: https://make.fun/bounty/news-image-20261124

Bounty: `news-image-20261124` (make.fun) · Akun 3 · Discord @cicihandayani

## Konsep
Halaman berita satu gambar dibingkai sebagai meja planetarium/orrery:
masthead "THE ORRERY — Tuesday's World in One Picture", palet tembaga /
biru gelap di atas krem, cincin orbit tipis di masthead, nomor kartu dalam
cincin kecil. Lead trio: #17 UN AI weapons · #15 FBI probe · #2 Sparta II.
Semua cerita dari pool terkunci Selasa 24 November 2026 (angka induk pool,
dipakai verbatim); tidak ada cerita yang dikarang, tidak ada item NI22/NI23
yang dipakai sebagai berita.

## Entry
- Dimensi: **1024 × 1024 px** (lolos gate server)
- Ukuran: **445.295 byte**
- sha256: **6c40cd4a79ca6c5aa0cb557547ec5a934cd186698c86c49f74ff5dad4d2475cb**
- `main.py` — carrier stdlib-only: verifikasi signature PNG + dimensi IHDR,
  MENOLAK gambar yang melanggar gate 1024×1024, salin byte-for-byte ke
  `MAKEFUN_OUTPUT_DIR` (fallback /output), verifikasi salinan identik.
- `compose.py` — renderer PIL (stdlib + PIL): 3 varian (A/B/C) + duel
  internal, pemenang (A) difinalisasi ke `entry.png` 1024×1024.
- Margin: **13/13 LOLOS** (`margin_check.py --fresh ni24-fresh.txt`)
- Isi: 15 kartu + 24 brief = **39 cerita**, 7 region, strip angka 8 item
  (semua mengikat kartu), strip region 7 region, timeline 6 slot (satu jam
  terverifikasi Selasa 04:24 WIB + day-part UTC), peta dunia titik-titik
  berpin bernomor 1–15, panel ALSO ON, kotak DATE CHECK 7 buangan bernama
  bertanggal, footer sumber + legenda kepastian + "Original drawings."

## Cara menjalankan
- `python3 compose.py` — render varian A/B/C (kanvas 3900×4288).
- `python3 compose.py final A` — finalisasi varian pemenang ke `entry.png`.
- `MAKEFUN_OUTPUT_DIR=out python3 main.py` — salin `entry.png` ke `out/`.

## Lisensi
MIT — lihat `LICENSE`.
