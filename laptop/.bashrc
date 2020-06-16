# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment and startup programs
export PATH=/home/vbmacher/.local/bin:/home/vbmacher/bin:/opt/robomongo/bin:/var/lib/snapd/snap/bin:$PATH
export JAVA_HOME=/usr/lib/jvm/java

export NO_NETRC=1
export QT_SCALE_FACTOR=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib

alias nexusmount="simple-mtpfs /mnt/nexus"
alias nexusumount="fusermount -u /mnt/nexus"

# Set config variables first
GIT_PROMPT_ONLY_IN_REPO=1

Time12a="\$(date +%H:%M)"
PathShort="\w";

GIT_PROMPT_START_USER="_LAST_COMMAND_INDICATOR_ ${Yellow}${PathShort}${ResetColor}"
GIT_PROMPT_START_ROOT="_LAST_COMMAND_INDICATOR_ ${GIT_PROMPT_START_USER}"

GIT_PROMPT_END_USER=" \n${White}${Time12a}${ResetColor} $ "
GIT_PROMPT_END_ROOT=" \n${White}${Time12a}${ResetColor} # "

. ~/bin/bash-git-prompt/gitprompt.sh
