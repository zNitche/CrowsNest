# CrowsNest
lightberryAPI + Raspberry Pi Pico W = LAN services hub

### Requirements
- Project utilize `lightberryAPI v1.2.1` as part of MicroPython firmware
[see](https://github.com/zNitche/lightberryAPI?tab=readme-ov-file#as-a-micropython-frozen-module)
- Project utilize [aht20.py](https://github.com/zNitche/pico-aht20/blob/master/aht20.py) as part of MicroPython firmware

### Extra
#### Database tools
  - minify `db.json`
  ```
  python3 .tools/convert_db.py --db_path ./db.json --minify
  ```
  - de-minify `db.json`
  ```
  python3 .tools/convert_db.py --db_path ./db.json
  ```
