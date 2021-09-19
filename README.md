# dotfig
Easily sync, store, edit and backup your dotfiles and configs 

to use just type dotfig at the cli + the name of the directory containing your dotfiles
ex: dotfig dotfiles
it will then create sym links to the home folder and all parents dirs, it will not overwrite existing configs / it will rename them to file_old

install options:

1:
clone the repo and run pip install -e /path/to/script/folder
-e stands for editable, meaning you'll be able to work on the script and invoke the latest version without need to reinstall
After that you can run myscript from any directory.

2:
With git
pip install git+https://github.com/DevAtDawn/dotfig.git
pip install git+ssh://git@github.com:DevAtDawn/dotfig.git

problem on Linux is that pip install ... drops scripts into ~/.local/bin and this is not on the default Debian/Ubuntu $PATH
add ~/.local/bin to your $PATH, for example by adding the following line to your .bashrc file:
export PATH="$HOME/.local/bin:$PATH"


Without git
pip install


https://stackoverflow.com/questions/8247605/configuring-so-that-pip-install-can-work-from-github
