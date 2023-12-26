from dataclasses import dataclass

@dataclass
class EnergyInvoiceDTO:
    client_id: int
    invoice_date: str
    reference_month: str
    electrical_energy_quantity: float
    electrical_energy_amount: float
    electrical_energy_scee_quantity: float
    electrical_energy_scee_amount: float
    electrical_energy_gdi_quantity: float
    electrical_energy_gdi_amount: float
    municipal_public_lighting_contribution: float
