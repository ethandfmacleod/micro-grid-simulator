from django.db import models

class BaseType(models.TextChoices):
    EnergyIn = "energy_in"
    EnergyOut = "energy_out"
    EnergyStorage = "energy_storage"

class ObjectType(models.TextChoices):
    SolarPanel = "solar_panel"
    WindTurbine = "wind_turbine"
    FactoryModel = "factory_model"
    ComplexHome = "complex_home"
    GeneralConsumer = "general_consumer"
    LithiumIon = "lithium_ion"

class SolarPanelType(models.TextChoices):
    Default = "default"

class SolarPanelMaterial(models.TextChoices):
    Default = "default"

class DisplayType(models.TextChoices):
    numeric = "numeric"
    dropdown = "dropdown"
    checkbox = "checkbox"
    segmented = "segmented"
    text = "text"