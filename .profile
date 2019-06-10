if [ -n "$BASH" ] && [ -r ~/.bashrc ]; then
    . ~/.bashrc
fi

export PATH="$HOME/.cargo/bin:$PATH"
