#Referenced 'https://medium.com/@mounirboulwafa/creating-a-single-executable-file-exe-from-a-python-program-abda6a41f74f'

target:
	pip install pyinstaller
	pyinstaller --onefile --windowed arith.py
	mv dist/arith .

