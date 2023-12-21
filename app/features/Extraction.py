import os
import pdfplumber
from typing import List

from services.IExtract import IExtract
from services.ExtractFromString import ExtractFromString
from services.IExport import IExport
from services.ExportToPostgreSQL import ExportToPostgreSQL
from services.ExportToJSON import ExportToJSON
from dtos.EnergyInvoiceDTO import EnergyInvoiceDTO

class Extraction:
    
    def __init__(self, args):
        self._validate_arguments(args)

        self.input: str = args.input
        self.output: str = args.output

        self.extraction_algorithm: IExtract = ExtractFromString()
        self.export_algorithm: IExport = ExportToPostgreSQL()

    def execute(self):
        extracted_data = self._extract_data()
        self.export_algorithm.export(extracted_data)

    def _extract_data(self) -> List[EnergyInvoiceDTO]:
        data_to_save = []

        for file_name in os.listdir(self.input):
            if file_name.endswith('.pdf'):
                pdf_path = os.path.join(self.input, file_name)

                with pdfplumber.open(pdf_path) as pdf:
                    page = pdf.pages[0]
                    extract = self.extraction_algorithm.extract(page)
                    data_to_save.append(extract)

        return data_to_save

    def _validate_arguments(self, args):
        if not args.input or not args.output:
            raise Exception("The --input and --output arguments are required when using the --convert option.")
        
        if not os.path.exists(args.input):
            raise Exception(f"The directory {args.input} does not exist.")
