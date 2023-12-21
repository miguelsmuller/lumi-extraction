from pdfplumber.page import Page

from services.IExtract import IExtract
from dtos.EnergyInvoiceDTO import EnergyInvoiceDTO

class ExtractFromString(IExtract):
    def __init__(self):
        pass
        
    def extract(self, data: Page) -> EnergyInvoiceDTO:
        text = data.extract_words()
        
        client_id = ""
        reference_month = ""
        electrical_energy_amount = ""
        electrical_energy_value = ""
        electrical_energy_scee_amount = ""
        electrical_energy_scee_value = ""
        electrical_energy_gdi_amount = ""
        electrical_energy_gdi_value = ""
        municipal_public_lighting_contribution = ""

        energy_invoice = {
            "client_id": client_id,
            "reference_month": reference_month,
            "electrical_energy_amount": electrical_energy_amount,
            "electrical_energy_value": electrical_energy_value,
            "electrical_energy_scee_amount": electrical_energy_scee_amount,
            "electrical_energy_scee_value": electrical_energy_scee_value,
            "electrical_energy_gdi_amount": electrical_energy_gdi_amount,
            "electrical_energy_gdi_value": electrical_energy_gdi_value,
            "municipal_public_lighting_contribution": municipal_public_lighting_contribution
        }

        return EnergyInvoiceDTO(**energy_invoice)
