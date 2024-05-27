#!/bin/bash

function flagunzip {
    echo '[+] UNZIP'
    mv flag flag.zip
    unzip flag.zip
    rm flag.zip
}

function flagbunzip {
    echo '[+] BZIP2'
    mv flag flag.bz2
    bzip2 -d flag.bz2
}

function flaggunzip {
    echo '[+] GUNZIP'
    mv flag flag.gz
    gunzip -f flag.gz
}

function flaguntar {
    echo '[+] TAR'
    mv flag flag.tar
    tar -xf flag.tar
    rm flag.tar
    #mv $(tar -tf flag.tar | head -n 1) flag
}

function flagbase64 {
    echo '[+] BASE64'
    tail flag
    echo -e '\n'
    read -r -p "Final decrypt? [Y/n] " response
    if [[ "$response" =~ ^([nN])+$ ]]
    then
    	exit
    else
    	base64 -d flag > flag.txt
        tail flag.txt
    	rm flag
    fi
}

while :
do
    filetype=$(file -b flag | awk '{print $1}')
    case "$filetype" in
   	  ASCII)
        flagbase64
        ;;
   	  gzip)
        flaggunzip
        ;;
   	  bzip2)
        flagbunzip
        ;;
   	  Zip)
        flagunzip
   		;;
      POSIX)
        flaguntar
        ;;
      *)
   		 echo "Done!"
   		 exit
    esac
#    sleep 2
done