#!/usr/bin/env bash

export_png() {
  if [ -f "pinout_deca.png" ]; then
    rm pinout_deca.png
  fi
  python3 -m pinout.manager --export pinout_deca pinout_deca.png
#  python3 -m pinout.manager --export pinout_deca_offset pinout_deca_offset.png
}

watch() {
  while true; do
    inotifywait -e modify styles.css pinout_deca.py data.py
    echo "Change!"
    export_png
  done
}

case "$1" in
'w')
  watch
  ;;
*)
  export_png
  ;;
esac
