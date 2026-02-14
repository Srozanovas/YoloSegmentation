python -m venv Libraries
call Libraries\Scripts\activate
pip uninstall -y torch torchvision torchaudio
pip install --index-url https://download.pytorch.org/whl/cu121 torch torchvision torchaudio
pip install ultralytics