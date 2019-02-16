#!binbash
echo -e "\e[3J"
echo "LazySource Version: "
lynx --dump pastebin.com/raw/JN9RC4Wj > version.txt
while read line; do echo $line; done < version.txt
