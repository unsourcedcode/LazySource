#!binbash
printf "\033c"
echo -e "Made by Vaxure | LazySource Version\n"
echo -e "Tool for pen-testing access your tools faster and easier for beginners.\nalso updates your pentesting tools every time you start it."
echo -e "\n\nLazySource Last Version: "
lynx --dump pastebin.com/raw/JN9RC4Wj > version.txt
while read line; do echo $line; done < version.txt
echo -e "\n\nLazySource News: "
lynx --dump pastebin.com/raw/fvr6QC8X > news.txt
while read line; do echo $line; done < news.txt
