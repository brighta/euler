#! /bin/zsh

if [ -z "$1" ]; then
  printf "\033[1;31mYou must provide a Problem Number.\033[0m"
  exit 1
fi

problem_number=$1

git add --all
git commit -m "Added problem ${problem_number}."
git push
