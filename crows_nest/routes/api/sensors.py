from lightberry import Router, Response
from lightberry.shortcuts import jsonify
from crows_nest import sensors_cache


sensors_api = Router("sensors_api", url_prefix="/api/sensors")


@sensors_api.route("/environment")
async def environment_data(request):
    aht20_data = sensors_cache.read("aht20")
    temp = None
    humidity = None

    if aht20_data:
        temp = aht20_data.get("temperature")
        humidity = aht20_data.get("humidity")

    data = {
        "temperature": temp,
        "humidity": humidity
    }

    return Response(payload=jsonify(data))
