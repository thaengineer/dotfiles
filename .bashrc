# if not running interactively, do nothing
[[ $- != *i* ]] && return

# shell appearance
PS1='\[\033[01;34m\][\u]\[\033[01;31m\][\h]\[\033[01;34m\][\W]\[\033[01;37m\] $ 33[00m\]'

# path
export PATH=${PATH}:${HOME}/.bin
export WINEPREFIX=${HOME}/.wine

# aliases
. ${HOME}/.aliases
