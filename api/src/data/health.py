import hashlib
import random

from faker import Faker

from src.schemas.response import HealthData
from src.data.factories import HealthDataFactory, WarningHealthDataFactory, DangerHealthDataFactory

_SCENARIO_MAP = {
    "warning": WarningHealthDataFactory,
    "danger":  DangerHealthDataFactory,
}


def _seed_from_uuid(patient_id: str) -> int:
    return int(hashlib.md5(patient_id.encode()).hexdigest(), 16) % (10 ** 9)


def get_health_data(patient_id: str) -> HealthData:
    factory_cls = _SCENARIO_MAP.get(patient_id, HealthDataFactory)
    seed = _seed_from_uuid(patient_id)

    Faker.seed(seed)
    random.seed(seed)
    
    return factory_cls.build()