import re


class Features:
    """FeatureInfo
    """

    headers = None
    src_chamber = '*chamber'
    src_start = '*start_time'

    sensors = list()
    sensors_oes = list()
    steps = list()
    steps_oes = list()
    stats = list()
    stats_oes = list()

    flag_oes_exists = False

    headers_feature = None
    headers_others = None

    pattern_feature = re.compile(r'^([^_]+)_(\d+)_(.+)$')
    pattern_oes = re.compile(r'^\d+\.\d+nm$')

    def __init__(self, headers: list):
        self.headers = headers
        self.init_sensor()

    def init_sensor(self):
        """extract sensor information
        """
        self.headers_feature = [s for s in self.headers if not s.startswith('*')]
        self.headers_others = [s for s in self.headers if s.startswith('*')]
        # _____________________________________________________________________
        # Step, Sensor, Stat
        sensors = list()
        sensors_oes = list()
        steps = list()
        steps_oes = list()
        stats = list()
        stats_oes = list()
        dict_features = {
            'sensors': sensors,
            'sensors_oes': sensors_oes,
            'steps': steps,
            'steps_oes': steps_oes,
            'stats': stats,
            'stats_oes': stats_oes,
        }
        for feature in self.headers_feature:
            self.sensor_step(feature, dict_features)
        # _____________________________________________________________________
        # Unique, Sort
        self.sensors = sorted(list(set(dict_features['sensors'])))
        self.steps = sorted(list(set(dict_features['steps'])))
        self.stats = sorted(list(set(dict_features['stats'])))
        if len(dict_features['sensors_oes']) > 0:
            self.setOESExists(True)
            self.sensors_oes = sorted(list(set(dict_features['sensors_oes'])))
            self.steps_oes = sorted(list(set(dict_features['steps_oes'])))
            self.stats_oes = sorted(list(set(dict_features['stats_oes'])))
        else:
            self.setOESExists(False)

    def sensor_step(self, feature, dict_features: dict):
        """separate sensor, step and stat from feature
        """
        result_all = self.pattern_feature.match(feature)
        if result_all:
            sensor = result_all.group(1)
            step = int(result_all.group(2))
            stat = result_all.group(3)
            result_oes = self.pattern_oes.match(sensor)
            if result_oes:
                dict_features['sensors_oes'].append(sensor)
                dict_features['steps_oes'].append(step)
                dict_features['stats_oes'].append(stat)
            else:
                dict_features['sensors'].append(sensor)
                dict_features['steps'].append(step)
                dict_features['stats'].append(stat)

    # _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_

    def getHeaders(self) -> list:
        """get/return original header list
        """
        return self.headers

    def getOESSensors(self) -> list:
        """get/return OES sensor list
        """
        return self.sensors_oes

    def getOESStats(self) -> list:
        """get/return OES stat list
        """
        return self.stats_oes

    def getOESSteps(self) -> list:
        """get/return OES steps
        """
        return self.steps_oes

    def getSensors(self) -> list:
        """get/return sensor list
        """
        return self.sensors

    def getStats(self) -> list:
        """get/return stat list
        """
        return self.stats

    def getSteps(self) -> list:
        """get/return recipe steps
        """
        return self.steps

    def isOESExists(self):
        return self.flag_oes_exists

    def setOESExists(self, flag: bool):
        self.flag_oes_exists = flag
