#! /bin/zsh

if [ -z "$1" ]; then
  printf "\033[1;31mYou must provide a Problem Number.\033[0m"
  exit 1
fi

problem_number=$1
parameter=$2

clear;time /opt/homebrew/bin/python3 "${problem_number}.py" $parameter

