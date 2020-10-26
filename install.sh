echo "
  █████   ██████  █████ █████  ██████  ████████  
 ███░░   ███░░███░░███ ░░███  ███░░███░░███░░███ 
░░█████ ░███████  ░███  ░███ ░███████  ░███ ░███ 
 ░░░░███░███░░░   ░░███ ███  ░███░░░   ░███ ░███ 
 ██████ ░░██████   ░░█████   ░░██████  ████ █████
░░░░░░   ░░░░░░     ░░░░░     ░░░░░░  ░░░░ ░░░░░  (created by omar salah)
                                                ";
echo "";
echo "[✔] You want to install seven in the system [Y/N] :" ;
read bello
if [ $bello == "y" ] ;
  then
    echo " "
  else
    exit
fi

echo "[✔] Where Do you want to install seven ? [Ex:/usr/share/doc]:";
read kebl
echo "[✔] Checking directories..."
if [ -d "$kebl/fsociety" ] ;
then
echo "[◉] A directory fsociety was found! Do you want to replace it? [Y/n]:" ; 
read mamido
if [ $mamido == "y" ] ; 
then
 rm -R "$kebl/seven"
else
 exit
fi
fi

 echo "[✔] Installing ...";
 echo "";
 git clone https://github.com/OmarSalah413/SeVen.git $kebl/seven;
 echo "#!/bin/bash 
 python $kebl/seven/SeVen.py" '${1+"$@"}' > seven;
 chmod +x SeVen.py;
 sudo cp seven /usr/bin/;
 rm seven;


if [ -d "$kebl/seven" ] ;
then
echo "";
echo "[✔]Seven installed with success![✔]";
echo "";
  echo " /    ✔    \ ";
  echo " \type seven/ ";
  echo "  \        /  ";
  echo "";
else
  echo "[✘] Installation faid![✘] ";
  exit
fi