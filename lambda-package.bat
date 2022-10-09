pip install --platform manylinux2014_x86_64 --target=./lambda/ --implementation cp --python 3.9 --only-binary=:all: --upgrade pandas 
pip install --platform manylinux2014_x86_64 --target=./lambda/ --implementation cp --python 3.9 --only-binary=:all: --upgrade entsoe-py 
pip install --platform manylinux2014_x86_64 --target=./lambda/ --implementation cp --python 3.9 --only-binary=:all: --upgrade numpy 
