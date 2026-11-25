# THE COPPERPLATE — NI24 Wave 2 · Akun 3 (@cicihandayani)

[![Bounty](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/cicihandayani530/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/cicihandayani530/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

Bounty: `news-image-20261124` (make.fun) · Akun 3 · GitHub @cicihandayani530

## Konsep

Satu hari berita dunia, Selasa 24 November 2026, diukir pada satu pelat
tembaga: halaman koran satu gambar bergaya copperplate engraving —
masthead serif besar di atas krem, strip angka induk di bawahnya, dan
bar region berwarna yang menghitung semua cerita per kawasan.

- **36 cerita** tersaji dalam satu halaman: **13 kartu adegan** bernomor
  plus 23 brief bernomor di panel "Also on the Plate".
- **9 region terlabel semua**: Europe, Middle East, Africa, Americas,
  Asia, South Asia, Asia-Pacific, Oceania, World — bar region 9/9.
- **Lead hard-news**: #1 Merkury (Ukraine sinks Russian warship off
  Benghazi), #4 COP31 (ends with NO DEAL — first since 2000), #6 Gaza
  (Israeli strikes kill 3, incl. UNRWA worker).
- Angka induk pool, verbatim: Gold **$3,588** · Bitcoin **61,284** ·
  US House **258–173** · Liverpool **4–0** · GTA VI Day 1 **$3.8BN**.
- Panel "Date Check — Not Today" menyingkirkan cerita lama secara
  eksplisit; setiap cerita berasal dari pool sah hari itu, tanpa hype.
- Setiap kartu ditutup footer REPORTED dengan nama wire konfirmasi.

## Entry

- Dimensi: **1024 × 1024 px** (lolos gate server)
- Ukuran: **258.414 byte**
- sha256: **fb95d06bc26f7a06a2fae6f44205a491b59557026dec5a33243525714df1f357**
- `main.py` — carrier stdlib-only: verifikasi signature PNG + dimensi
  IHDR + batas 1 MiB, lalu menulis byte `entry.png` persis sebagai
  keluaran.
- Craft: clip-layer per kartu di semua 13 kartu — polyline Bitcoin tetap
  di dalam kartu #9, elips matahari COP31 ter-clip di bingkai kartunya,
  sparkline tidak menyentuh footer REPORTED kartu #2/#3.
- Verifikasi ulang mandiri sebelum push: kata "language" pada kartu
  COP31 terbaca utuh di dalam bingkai, strip timeline UTC menampilkan
  "(AP)" secara lengkap, dan footer REPORTED kartu Kyiv #3 serta
  Sparta II #2 bersih tanpa luapan — diperiksa crop-zoom per zona.
