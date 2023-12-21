from dataclasses import dataclass

@dataclass
class EnergyInvoiceDTO:
    client_id: int
    reference_month: str
    electrical_energy_amount: float
    electrical_energy_value: float
    electrical_energy_scee_amount: float
    electrical_energy_scee_value: float
    electrical_energy_gdi_amount: float
    electrical_energy_gdi_value: float
    municipal_public_lighting_contribution: float
