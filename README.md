# CrowsNest
lightberryAPI + Raspberry Pi Pico W = LAN services hub

### Requirements
- Project utilize `lightberryAPI v1.2.1` as part of MicroPython firmware
[see](https://github.com/zNitche/lightberryAPI?tab=readme-ov-file#as-a-micropython-frozen-module)
- Project utilize [aht20.py](https://github.com/zNitche/pico-aht20/blob/master/aht20.py) as part of MicroPython firmware

### Features:
- Providing API + serving services data for [web ui](https://github.com/zNitche/CrowsNestUI).
- Logging environment temperature and humidity.
- Serving React based frontend.
- Build in database supporting data sorting and querying.
- Database models serialization.
- Simple cache implementation.
- Checking services accessibility.

### How to use it:
1. Build (and flash rpi pico with) MicroPython firmware with modules described in `Requirements` section.
2. Build and prepare (described in README) [web ui](https://github.com/zNitche/CrowsNestUI).
3. Copy content of web ui `dist` to `/files` directory.
4. Create and fill `lightberryAPI` config.
```
cp lightberry_config.template.json lightberry_config.json
```
5. Create and fill database.
```
cp db.template.json db.json
```
6. Flash Raspberry Pi Pico with this project files.

### Project Goals:
The main goals of the project was to: 
- Use lightberryAPI in real case scenario.
- Build low power consumption device I can use to track LAN services.
- Design and print 3D case.

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
