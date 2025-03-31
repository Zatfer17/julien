<p align="center">
  <img src="https://static.wikia.nocookie.net/penguinsofmadagascar/images/a/ad/Julien-character-web-desktop.png/revision/latest/scale-to-width/360?cb=20190718042749" width="200" align="center"/>
</p>

# `julien`

Download [Boiler Room](https://www.youtube.com/@boilerroom) sets as `m4a`s straight to your local music folder.

## Usage

1. Clone the repo:
```
git clone https://github.com/Zatfer17/julien
```

2. Create and activate a virtual environment:
```
python -m venv .venv
source .venv/bin/activate
```

3. Install the requirements:
```
pip install -r requirements.txt
```

4. Optionally edit the script config in `main.py`:
```python
MUSIC_PATH    = Path.home() / "Music" / "Boiler Room"
URL           = "https://www.youtube.com/@boilerroom"
TITLE_FILTER  = "| Boiler Room"
LENGTH_FILTER = 2700
VIEWS_FILTER  = 1000000
```

5. Run the script:
```
python main.py
```