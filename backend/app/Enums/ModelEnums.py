from django.db import models

class BaseType(models.TextChoices):
    EnergyIn = "energy_in"
    EnergyOut = "energy_out"
    EnergyStorage = "energy_storage"

class ObjectType(models.TextChoices):
    SolarPanel = "solar_panel"
    WindTurbine = "wind_turbine"
    FactoryModel = "factory_model"
    Home = "home"
    GeneralConsumer = "general_consumer"
    LithiumIon = "lithium_ion"
    Inverter = "inverter"
    Grid = "grid"

class SolarPanelType(models.TextChoices):
    Residential = "Residential"
    Commercial = "Commercial"

class SolarPanelMaterial(models.TextChoices):
    Monocrystalline  = "Monocrystalline"
    Polycrystalline = "Polycrystalline"
    ThinFilm = "Thin-Film"

class CalculationMode(models.TextChoices):
    Outputs = "Outputs"
    Advanced = "Advanced"
    SolarPowerBased = "Power Based"
    SolarPeakSunlightHours = "Peak Sunlight Hours"
    SolarElectrical = "Electrical"
    SolarPhysical = "Physical"
    WindPowerOutput = "Power Output"
    WindRotorBased = "Rotor Based"
    WindCutInCutOutSpeeds = "Cut In/Out Speeds"
    SimpleHome = "Simple Home"
    ComplexHome = "Complex Home"
    BatteryManagement = "Battery Management"
    BatteryPerformance = "Battery Performance"
    InverterEfficiency = "Inverter Efficiency"
    GridUsage = "Grid Usage"

class DisplayType(models.TextChoices):
    numeric = "numeric"
    dropdown = "dropdown"
    checkbox = "checkbox"
    segmented = "segmented"
    list = "list"
    text = "text"