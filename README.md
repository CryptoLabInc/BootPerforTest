# BootPerformTest


## lattigo

```shell
git clone https://github.com/tuneinsight/lattigo
cd lattigo
```

- Put the file '/lattigo/main.go' to (latttigo directory)

```shell
go run main.go
```



## liberate-fhe

```shell
git clone https://github.com/Desilo/liberate-fhe
cd liberate-fhe
```

- Put the file '/liberate/mult_time.py' to (liberate-fhe directory)

```shell
python mult_time.py
```



## openfhe-development

```shell
git clone https://github.com/openfheorg/openfhe-development
cd openfhe-development
```

- Change the files
  /openfhe-development/src/pke/CMakeLists.txt,
  /openfhe-development/src/pke/extras/ckks-bootstrap.cpp
  to the files in this repo.

```shell
mkdir build
cd build
cmake ..
make -j
bin/example/pke/ckks-bootstrap
```
