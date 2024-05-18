#!/bin/sh

input_folder="./"

for file in "$input_folder"/*; do
    # 找出資料夾中的影片
    if [ -f "$file" ] && file --mime-type "$file" | grep -q "video"; then
        filename=$(basename -- "$file")
        extension="${filename##*.}"
        filename="${filename%.*}"

        # 使用 FFmpeg 鏡像影片
        ffmpeg -i "$file" -vf hflip -acodec copy "./${filename}_mirrored.$extension"
    fi
done

