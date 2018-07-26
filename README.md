## Usage
- Go the folder specific to your distribution 
- Execute the following on terminal/commandline: `./im_filter "<program to run>" "<input image path>"`
- A new image called: `new_image.png` will be created with the output

### building binaries

```bash
    sudo docker run --rm -it -v "$PWD":/usr/src/myapp -w /usr/src/myapp golang bash
    ./build.sh ./mat_to_img/
    ./build.sh ./img_to_mat/
```

Now each folder is ready for distribution :)
