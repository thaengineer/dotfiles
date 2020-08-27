# if not running interactively, do nothing
[[ $- != *i* ]] && return

# shell appearance
PS1='\[\033[01;34m\][\u]\[\033[01;31m\][\h]\[\033[01;34m\][\W]\[\033[01;37m\] $ 33[00m\]'

# path
if [ -d ${HOME}/.bin ]; then
  export PATH=${PATH}:${HOME}/.bin
fi
if [ -d ${HOME}/.wine ]; then
  export WINEPREFIX=${HOME}/.wine
fi

# aliases
. ${HOME}/.aliases
