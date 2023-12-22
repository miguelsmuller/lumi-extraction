import os

from pdfplumber.page import Page

from services.IExtract import IExtract
from dtos.EnergyInvoiceDTO import EnergyInvoiceDTO

class ExtractFromJSON(IExtract):
    def __init__(self):
        pass
        
    def extract(self, data: Page, file_name, file_path) -> EnergyInvoiceDTO:
        image = data.to_image()
        image.draw_rects(data.extract_words())
        image_path = os.path.join(file_path, f"{file_name}.png")

        print(image_path)
        #image.save(image_path, format="PNG")
        
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
