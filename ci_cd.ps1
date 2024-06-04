Write-Output "Running tests with Pytest..."
& .\.venv\Scripts\python.exe -m pytest --html=report.html --self-contained-html

Write-Output "Checking code style with Flake8..."
& .\.venv\Scripts\flake8.exe --config=D:\labsss\minesweeper\inst\flake.flake8 --format=html --htmldir=flake-report
