import abc
from typing import List
from pdfplumber.page import Page

from dtos.EnergyInvoiceDTO import EnergyInvoiceDTO

class IExtract(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def extract(self, data: Page) -> EnergyInvoiceDTO:
        pass
