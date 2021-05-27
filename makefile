all:
	python3 setup.py build_ext --inplace
	mkdir outputs
clean:
	rm -rf build *.so cyfib.c *.c *.html outputs *.png