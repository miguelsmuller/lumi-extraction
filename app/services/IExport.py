import abc
from typing import List

from dtos.EnergyInvoiceDTO import EnergyInvoiceDTO

class IExport(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def export(self, output:str, energy_invoices: List[EnergyInvoiceDTO]) -> None:
        pass
