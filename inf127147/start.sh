#!/bin/bash

input_path=$(realpath $1)
output_path=$(realpath $2)
path_to_algorithm=$(realpath $0)
dir_to_algorithm=$(dirname $path_to_algorithm)
path_to_algorithm="$dir_to_algorithm/List_algorithm.py"

python3 $path_to_algorithm $input_path $output_path
