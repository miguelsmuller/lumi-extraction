import os
import pdfplumber
from typing import List


from services.IExtract import IExtract
from services.ExtractFromString import ExtractFromString
from services.IExport import IExport
from services.ExportToJSON import ExportToJSON
from dtos.EnergyInvoiceDTO import EnergyInvoiceDTO

class Extraction:
    
    def __init__(self, args):
        self._validate_arguments(args)

        self.input: str = args.input
        self.output: str = args.output

        self.extraction_algorithm: IExtract = ExtractFromString()
        self.export_algorithm: IExport = ExportToJSON()

    def execute(self):
        self.export_algorithm.export(
            self.output, 
            self._extract_data()
        )

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
        
# # DEBUG DO PDF
# debug = page.extract_words()
# debug_file = os.path.splitext(file_name)[0]
# output_file_path = os.path.join(self.output, f"{debug_file}.json")

# with open(output_file_path, "w", encoding="utf-8") as json_file:
#     json.dump(debug, json_file, ensure_ascii=False, indent=4)

# # SALVA A IMAGEM
# image = page.to_image()
# image.draw_rects(page.extract_words())
# image_path = os.path.join(self.output, f"{file_name}.png")
# image.save(image_path, format="PNG")  
