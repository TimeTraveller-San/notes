# Problem 
You're going to get gcc compile errors while installing pytorch3d from source on latest (07/02/2020) build of arch (well updated).

# Fix
Downgrade binuitls
```
sudo pacman -U https://archive.archlinux.org/packages/b/binutils/binutils-2.30-5-x86_64.pkg.tar.xz
```

.... Why am I even using arch linux?
