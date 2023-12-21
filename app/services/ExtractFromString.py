import locale
from pdfplumber.page import Page

from services.IExtract import IExtract
from dtos.EnergyInvoiceDTO import EnergyInvoiceDTO

class ExtractFromString(IExtract):
    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    def extract(self, data: Page) -> EnergyInvoiceDTO:
        text = data.extract_text()
        
        client_id_index = text.find("Nº DO CLIENTE")
        client_id = text[client_id_index + 53:client_id_index + 64].strip()

        reference_month_index = text.find("Referente a")
        reference_month = text[reference_month_index + 62:reference_month_index + 71].strip()

        electrical_energy_amount_index = text.find("Energia Elétrica")
        electrical_energy_amount = text[electrical_energy_amount_index + 21:electrical_energy_amount_index + 23].strip()

        electrical_energy_value_index = text.find("Energia Elétrica")
        electrical_energy_value = text[electrical_energy_value_index + 34:electrical_energy_value_index + 40].strip()                    
        
        electrical_energy_scee_amount_index = text.find("Energia SCEE s/ ICMS")
        electrical_energy_scee_amount = text[electrical_energy_scee_amount_index + 25:electrical_energy_scee_amount_index + 30].strip()

        electrical_energy_scee_value_index = text.find("Energia SCEE s/ ICMS")
        electrical_energy_scee_value = text[electrical_energy_scee_value_index + 42:electrical_energy_scee_value_index + 48].strip()

        electrical_energy_gdi_amount_index = text.find("Energia compensada GD I")
        electrical_energy_gdi_amount = text[electrical_energy_gdi_amount_index + 28:electrical_energy_gdi_amount_index + 33].strip()

        electrical_energy_gdi_value_index = text.find("Energia compensada GD I")
        electrical_energy_gdi_value = text[electrical_energy_gdi_value_index + 45:electrical_energy_gdi_value_index + 52].strip()

        municipal_public_lighting_contribution_index = text.find("Contrib Ilum Publica Municipal")
        municipal_public_lighting_contribution = text[municipal_public_lighting_contribution_index + 31:municipal_public_lighting_contribution_index + 36].strip()

        energy_invoice = {
            "client_id": client_id,
            "reference_month": reference_month,
            "electrical_energy_amount": locale.atof(electrical_energy_amount),
            "electrical_energy_value": locale.atof(electrical_energy_value),
            "electrical_energy_scee_amount": locale.atof(electrical_energy_scee_amount),
            "electrical_energy_scee_value": locale.atof(electrical_energy_scee_value),
            "electrical_energy_gdi_amount": locale.atof(electrical_energy_gdi_amount),
            "electrical_energy_gdi_value": locale.atof(electrical_energy_gdi_value),
            "municipal_public_lighting_contribution": locale.atof(municipal_public_lighting_contribution)
        }

        return EnergyInvoiceDTO(**energy_invoice)
