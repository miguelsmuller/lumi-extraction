import locale
from pdfplumber.page import Page
import os

from services.IExtract import IExtract
from dtos.EnergyInvoiceDTO import EnergyInvoiceDTO

class ExtractFromCroppedImage(IExtract):
    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    def extract(self, data: Page) -> EnergyInvoiceDTO:
        client_id = self._extract_from_partial(data, 14, 149, 120, 162)
        reference_month = self._extract_from_partial(data, 240, 65, 345, 75)
        electrical_energy_quantity = self._extract_from_partial(data, 210, 243, 230, 252)
        electrical_energy_amount = self._extract_from_partial(data, 300, 243, 340, 252)
        electrical_energy_scee_quantity = self._extract_from_partial(data, 210, 253, 230, 259)
        electrical_energy_scee_amount = self._extract_from_partial(data, 300, 253, 340, 259)
        electrical_energy_gdi_quantity = self._extract_from_partial(data, 210, 263, 230, 270)
        electrical_energy_gdi_amount = self._extract_from_partial(data, 300, 263, 340, 270)
        municipal_public_lighting_contribution = self._extract_from_partial(data, 300, 273, 340, 279)

        energy_invoice = {
            "client_id": client_id,
            "reference_month": reference_month,
            "electrical_energy_quantity": locale.atof(electrical_energy_quantity),
            "electrical_energy_amount": locale.atof(electrical_energy_amount),
            "electrical_energy_scee_quantity": locale.atof(electrical_energy_scee_quantity),
            "electrical_energy_scee_amount": locale.atof(electrical_energy_scee_amount),
            "electrical_energy_gdi_quantity": locale.atof(electrical_energy_gdi_quantity),
            "electrical_energy_gdi_amount": locale.atof(electrical_energy_gdi_amount),
            "municipal_public_lighting_contribution": locale.atof(municipal_public_lighting_contribution)
        }

        return EnergyInvoiceDTO(**energy_invoice)


    def _extract_from_partial(self, data, x0, top, x1, bottom):
        # 0,   0,  595,    842
        # x0, top,  x1,  bottom
        
        page_cutout = data.crop((x0, top, x1, bottom))
        return page_cutout.extract_text()
