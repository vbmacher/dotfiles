# My Linux dotfiles

## Fedora

### Vim

```
dnf install vim
cp bigpc/.vimrc ~/.vimrc
```

### Git

```
dnf install git
cp bigpc/.gitconfig ~/.gitconfig

# https://github.com/magicmonty/bash-git-prompt
git clone https://github.com/magicmonty/bash-git-prompt.git ~/.bash-git-prompt --depth=1
```

### Bash

```
cp bigpc/.bash_profile ~/.bash_profile
cp bigpc/.bashrc ~/.bashrc

dnf install rxvt-unicode
git clone https://github.com/janoamaral/Xresources-themes.git ~/.Xresources-themes --depth=1
cp bigpc/.Xresources ~/.Xresources
```

### SDKman!

```
curl -s "https://get.sdkman.io" | bash
```

### Browser

```
dnf install brave
dnf install firefox
dnf install chromium
```

### i3 window manager

```
dnf install maim       # cmdline screenshot
dnf install rofi       # dmenu replacement
dnf install pasystray  # pulse audio volume control tray icon
dnf install dolphin    # thunar replacement (nice file manager)
xdg-mime query default inode/directory
xdg-mime default org.kde.dolphin.desktop inode/directory
xdg-mime default thunar.desktop inode/directory
xdg-mime default dolphin.desktop inode/directory application/x-gnome-saved-search

dnf install mpd mpc  # music player
dnf install solaar   # logitech unifying usb receiver
dnf install network-manager-applet

dnf install i3
cp bigpc/.i3/ ~/.i3/

dnf install acpi sysstat
dnf install i3blocks   # https://github.com/vivien/i3blocks
cp bigpc/.i3blocks.conf ~/.i3blocks.conf
cp bigpc/bin/ ~/bin/


```





To install:




To clone:

- https://github.com/logico-dev/Xresources-themes



