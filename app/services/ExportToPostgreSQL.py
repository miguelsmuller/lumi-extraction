from typing import List
from dataclasses import asdict

from services.IExport import IExport
from models.EnergyInvoiceModel import EnergyInvoiceModel
from dtos.EnergyInvoiceDTO import EnergyInvoiceDTO
from config.DataBaseManager import DataBaseManager, Base

class ExportToPostgreSQL(IExport):
    def __init__(self): 
        with DataBaseManager() as db:
            Base.metadata.create_all(db.get_engine)

    def export(self, energy_invoices: List[EnergyInvoiceDTO]) -> None:
        with DataBaseManager() as db:
            for invoiceDTO in energy_invoices:
                invoiceModel = self._create_model_from_dto(invoiceDTO)

                db.session.add(invoiceModel)
            db.session.commit()

    def _create_model_from_dto(self, invoice: EnergyInvoiceDTO) -> EnergyInvoiceModel:
        return EnergyInvoiceModel(
            client_id=invoice.client_id,
            reference_month=invoice.reference_month,
            electrical_energy_quantity=invoice.electrical_energy_quantity,
            electrical_energy_amount=invoice.electrical_energy_amount,
            electrical_energy_scee_quantity=invoice.electrical_energy_scee_quantity,
            electrical_energy_scee_amount=invoice.electrical_energy_scee_amount,
            electrical_energy_gdi_quantity=invoice.electrical_energy_gdi_quantity,
            electrical_energy_gdi_amount=invoice.electrical_energy_gdi_amount,
            municipal_public_lighting_contribution=invoice.municipal_public_lighting_contribution
        )
