import json
import os

from typing import List
from dataclasses import asdict

from dtos.EnergyInvoiceDTO import EnergyInvoiceDTO
from services.IExport import IExport

class ExportToJSON(IExport):
    def __init__(self):
        pass
    
    def export(self, output:str, energy_invoices: List[EnergyInvoiceDTO]) -> None:
        self._create_output_directory(output)
        
        output_file_path = os.path.join(output, "resultado.json")

        invoices = [asdict(invoice) for invoice in energy_invoices]

        with open(output_file_path, "w", encoding="utf-8") as json_file:
            json.dump(invoices, json_file, ensure_ascii=False, indent=4)

    def _create_output_directory(self, output):
        if not os.path.exists(output):
            os.makedirs(output) 
