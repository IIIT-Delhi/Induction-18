# Image filtering

im_filter.py - the main script that will take care of everything
has a detailed help section. Accessible via python im_filter.py --help 

Also for full usage, use:
```bash
./im_filter "./a.out" logoTemp.jpg
```

Easter egg (The level switch, it will show expected output for that level, 1-8) :
```bash
./im_filter "./a.out" logoTemp.jpg -l 7
```

For detailed help:
```bash
./imfilter --help
```

# Deprecated go binaries, highly outdated
Use the im_filter binary instead (only for linux, ask windows people to share)

## building binaries

```bash
    sudo docker run --rm -it -v "$PWD":/usr/src/myapp -w /usr/src/myapp golang bash
    ./build.sh ./mat_to_img/
    ./build.sh ./img_to_mat/
```