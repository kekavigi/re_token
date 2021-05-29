# re_token

Modul Python untuk melakukan tokenisasi pada kalimat berbahasa Indonesia, dan mengubahnya kembali menjadi kalimat yang benar.

## Rencana

* [ ] Rapikan data:
  * [ ] Singkatan dalam format: SINGKATAN \t\t ARTI
  * [ ] Perbanyak data imbuhan
  * [ ] Tambah kata majemuk
  * [ ] Tambah kata dasar
  * [ ] Membuat daftar testcase

* [ ] Formatting yang mempermudah tahap-tahap selanjutnya
  * [ ] token dalam format: (`str`, `detail`={`type`, `obj-spec`})
  * [ ] Mengikutkan bentuk cetak miring dan cetak tebal

* [ ] Menambahkan fungsi fungsi dasar
  * [ ] ganti tipe token
  * [ ] memisahkan satu token
  * [ ] menggabung beberapa token
  * [ ] menambahkan/menghapus token
  
* [ ] Koreksi pada tingkat kata
  * [ ] perbaikan kata yang kemungkinan besar saltik
  * [ ] melakukan NER dan menyederhakannya menjadi satu token

* [ ] Koreksi pada tingkat kalimat
  * [ ] Tokenisasi kalimat
  * [ ] Pengecekan bentuk kata-kata terhadap aturan
  * [ ] `raise Error`

* [ ] Menampilkan hasil
  * [ ] Sentencizer
  * [ ] Website
  * [ ] Dokumentasi

## Data
* Daftar singkatan dari halaman Wiktionary Bahasa Indonesia [ini](https://id.wiktionary.org/w/index.php?title=Lampiran:Daftar_singkatan_dan_akronim_dalam_bahasa_Indonesia&oldid=967777).

* Daftar imbuhan
