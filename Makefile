.PHONY: build install

RELEASE_TYPE = Release

install:
	conan install . --build=missing

build: install
	cd build && cmake .. -DCMAKE_TOOLCHAIN_FILE=$(RELEASE_TYPE)/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=$(RELEASE_TYPE) -G Ninja
	cd build && cmake --build .

clean:
	rm -rf build
