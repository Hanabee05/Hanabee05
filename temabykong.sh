#!/bin/bash

# Bersihkan layar
clear

# Fungsi untuk menampilkan banner
banner() {
  echo -e "\e[1;44m"   # Latar belakang biru gelap
  echo -e "\e[1;37m"   # Teks putih terang
  echo "=================================="
  echo "      ASALAMU'ALAIKUM             "
  echo "=================================="
  echo ""
  echo -e "\e[92mAuthor  : UKONG GNTG"  # Hijau untuk nama author
  echo -e "\e[93mGithub  : https://github.com/Hanabee05"  # Kuning untuk Github
  echo -e "\e[96mTanggal : $(date)"  # Biru muda untuk tanggal
  echo -e "\e[0m"
}

# Memanggil fungsi banner
banner

# Fungsi untuk status baterai
battery_status() {
  termux-battery-status | grep "percentage" | awk '{print $2}' | tr -d ','
}

# Mengganti prompt dengan warna yang nyaman di mata
PS1="\e[1;36m\e[1;32m\u@\h\e[1;36m\e[0m [\$(date +%H:%M)] (\e[1;33m$(battery_status)%\e[0m) \e[1;37m\w\e[0m \$ "

# Mengaktifkan autocompletion dan auto-suggestion
if [ -f /data/data/com.termux/files/usr/etc/bash_completion ]; then
  . /data/data/com.termux/files/usr/etc/bash_completion
fi