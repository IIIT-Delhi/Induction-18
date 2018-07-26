#! /bin/bash

# linux x86-64 (64 bits)
img_to_mat/img_to_mat-linux-amd64 $2 | $1 | mat_to_img/mat_to_img-linux-amd64 

# linux x86 (32 bits)
#img_to_mat/img_to_mat-linux-386 $2 | $1 | mat_to_img/mat_to_img-linux-386

# windows x86-64 (64 bits)
#img_to_mat/img_to_mat-windows-amd64.exe $2 | $1 | mat_to_img/mat_to_img-windows-amd64.exe

# windows x86 (32 bits)
#img_to_mat/img_to_mat-windows-386.exe $2 | $1 | mat_to_img/mat_to_img-windows-386.exe