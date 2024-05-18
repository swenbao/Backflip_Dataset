#!/bin/zsh

# Define the range of directories to create and work with
start=0
end=6

# Copy rename.sh into each directory
for i in {${start}..${end}}; do
    cp rename.sh "$i+"
    cp rename.sh "$i-"
done

# Execute rename.sh in each directory
for i in {${start}..${end}}; do
    cd "$i+"
    chmod 777 ./rename.sh
    ./rename.sh
    cd ..

    cd "$i-"
    chmod 777 ./rename.sh
    ./rename.sh
    cd ..
done

