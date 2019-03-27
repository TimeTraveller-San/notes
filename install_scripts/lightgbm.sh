echo "Installing boost pacman packages"
sudo pacman -S boost-libs boost
echo "Cloning LGBM git repo: https://github.com/Microsoft/LightGBM"
git clone --recursive https://github.com/Microsoft/LightGBM
cd LightGBM
mkdir build
echo "Building lightgbm libraries"
cd build
cmake -DUSE_GPU=1 -DOpenCL_LIBRARY=/opt/cuda/lib64/libOpenCL.so -DOpenCL_INCLUDE_DIR=/opt/cuda/include/ ..
make -j$(nproc)
cd ..
echo "Installing python package"
cd python-package/
sudo python setup.py install --precompile
