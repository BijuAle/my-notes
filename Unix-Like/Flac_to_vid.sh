#! /bin/bash

srcExt=$1
destExt=$2

srcDir=$3
destDir=$4

opts=$5

for filename in "$srcDir"/*.$srcExt; do

        basePath=${filename%.*}
        baseName=${basePath##*/}
	
	ffmpeg -loop 1 -framerate 2 -i "Tiara.jpg" -i "$filename" -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a copy -shortest -pix_fmt yuv420p "$destDir"/"$baseName"."$destExt"

done

echo "Conversion from ${srcExt} to ${destExt} complete!"