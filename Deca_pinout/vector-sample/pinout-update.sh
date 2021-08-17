#!/usr/bin/env bash

#while  [ 1 -eq 1 ]; do 
  inotifywait -e modify styles.css pinout_deca.py data.py
  echo "Change!"
  rm pinout_deca.svg
#  python3 -m pinout.manager --export pinout_deca pinout_deca.svg
   python3 -m pinout.manager --export pinout_deca pinout_deca.png
#done
