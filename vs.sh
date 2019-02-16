#!binbash
printf "\033c"
echo "Made by Vaxure | LazySource Version"
echo "LazySource Last Version: "
lynx --dump pastebin.com/raw/JN9RC4Wj > version.txt
while read line; do echo $line; done < version.txt
