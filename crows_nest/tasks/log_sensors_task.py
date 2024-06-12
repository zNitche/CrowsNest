from lightberry import ATaskBase
from crows_nest import sensors_cache, machine_interfaces
from aht20 import AHT20


class LogSensorsTask(ATaskBase):
    def __init__(self, logging=False):
        super().__init__(periodic_interval=15, logging=logging)

        self.__aht20 = None

        self.__setup_modules()

    def __setup_modules(self):
        try:
            self.__aht20 = AHT20(machine_interfaces.i2c_0)

        except Exception as e:
            self.__print_log(message="error while performing modules setup", exception=e)

    def __log_ath20(self):
        if self.__aht20:
            temp = round(self.__aht20.get_temperature(), 1)
            humidity = round(self.__aht20.get_relative_humidity(), 1)

            sensors_cache.write("aht20", {"temperature": temp, "humidity": humidity})

    async def task(self):
        self.__log_ath20()
