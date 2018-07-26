## building binaries

```bash
    sudo docker run --rm -it -v "$PWD":/usr/src/myapp -w /usr/src/myapp golang bash
    ./build.sh ./mat_to_img/
    ./build.sh ./img_to_mat/
```

Now each folder is ready for distribution :)