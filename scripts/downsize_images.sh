# Usage: ./scripts/downsize_images.sh <DIRECTORY>

if [ $# -eq 0 ]
  then
    echo "Please provide a target directory"
    exit
fi

for f in $(ls $1); do
    file=$1$f
    before=$(identify -ping -format '%w %h' $file)
    size_before=$(stat --printf="%s" $file)
    convert $file -strip -resize 2000x2000\> $file
    after=$(identify -ping -format '%w %h' $file)
    size_after=$(stat --printf="%s" $file)
    echo "${file}: ${before} (${size_before}) -> ${after} (${size_after})"
done
