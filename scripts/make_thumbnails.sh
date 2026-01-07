# Usage: ./scripts/downsize_images.sh <DIRECTORY>/

if [ $# -eq 0 ]
  then
    echo "Please provide a target directory"
    exit
fi

for f in $(ls $1); do
    file=$1$f
    if [[ $(identify $file >/dev/null 2>/dev/null; echo $?) -ne 0 ]]
    then
      echo "Skipping ${file}"
      continue
    fi

    before=$(identify -ping -format '%w %h' $file)
    size_before=$(stat --printf="%s" $file)

    if [[ $file != *.jpg ]]
    then
      newfile=${file%.*}.jpg
      convert $file -format jpg $newfile
      rm $file
      file=$newfile
    fi

    mv $file "${file}_copy"
    convert "${file}_copy" -auto-orient -strip -thumbnail 1000\> $file
    rm "${file}_copy"

    after=$(identify -ping -format '%w %h' $file)
    size_after=$(stat --printf="%s" $file)
    echo "${file}: ${before} (${size_before}) -> ${after} (${size_after})"
done
