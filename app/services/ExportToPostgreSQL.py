from typing import List

from dtos.EnergyInvoiceDTO import EnergyInvoiceDTO
from services.IExport import IExport

class ExportToPostgreSQL(IExport):
    def __init__(self):
        pass
    
    def export(self, output:str, energy_invoices: List[EnergyInvoiceDTO]) -> None:
        pass
