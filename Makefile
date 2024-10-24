.PHONY: build install

RELEASE_TYPE = Release
PY_SRC = src/pysrc
CPP_SRC = src/cppsrc

install:
	conan install . --build=missing
	poetry install

build: install
	cd build && cmake .. -DCMAKE_TOOLCHAIN_FILE=$(RELEASE_TYPE)/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=$(RELEASE_TYPE) -G Ninja
	cd build && cmake --build .

test: build
	cd build && ./intern_tests
	poetry run pytest $(PY_SRC)/test

clean:
	rm -rf build

lint:
	poetry run mypy $(PY_SRC)
	poetry run ruff check $(PY_SRC)
	poetry run ruff format --check $(PY_SRC)

format:
	poetry run ruff format $(PY_SRC)
	poetry run ruff check --fix $(PY_SRC)
