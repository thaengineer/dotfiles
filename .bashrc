# if not running interactively, do nothing
[[ $- != *i* ]] && return

# shell appearance
if [ $(id -u) == 0 ]; then
  PS1='\033[01;34m[\u]\033[01;31m[\h]\033[01;34m[\W]\033[01;33m # \033[00m'
else
  PS1='\033[01;34m[\u]\033[01;31m[\h]\033[01;34m[\W]\033[01;37m $ \033[00m'
fi

# path
if [ -d ${HOME}/.bin ]; then
  export PATH=${PATH}:${HOME}/.bin
fi

# aliases
if [ -f ${HOME}/.aliases ]; then
  . ${HOME}/.aliases
fi

# wine
if [ -d ${HOME}/.wine ]; then
  export WINEPREFIX=${HOME}/.wine
fi
