from core import models


def approve_observation(observation: models.Observation):
    """Одобрение наблюдения"""
    observation.approved = True
    observation.status = True
    observation.save(update_fields=['approved', 'status'])


def refused_observation(observation: models.Observation):
    """Отказ в наблюдении"""
    observation.erroneous = False
    observation.status = True
    observation.save(update_fields=['erroneous', 'status'])
