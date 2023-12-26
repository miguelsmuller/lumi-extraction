from sqlalchemy import func, Column, Integer, Float, Date, String, TIMESTAMP
from datetime import datetime

from config.DataBaseManager import Base

class EnergyInvoiceModel(Base):
    __tablename__ = "invoices"

    id = Column(
        Integer, 
        primary_key=True, 
        autoincrement=True
    )
    
    client_id = Column(
        String,
        index=True
    )

    invoice_date = Column(
        Date,
        nullable=False
    )
    
    reference_month = Column(
        String, 
        index=True
    )
    
    electrical_energy_quantity = Column(
        Float
    )

    electrical_energy_amount = Column(
        Float
    )

    electrical_energy_scee_quantity = Column(
        Float
    )

    electrical_energy_scee_amount = Column(
        Float
    )

    electrical_energy_gdi_quantity = Column(
        Float
    )

    electrical_energy_gdi_amount = Column(
        Float
    )

    municipal_public_lighting_contribution = Column(
        Float
    )

    creation_at = Column(
        TIMESTAMP (timezone=True), 
        nullable=False, 
        server_default=func.now()
    )

    def parse_date(date_str):
        return datetime.strptime(date_str, '%d/%m/%Y').date()


    def __repr__(self):
        return "<Invoice (id='{}', client_id='{}', electrical_energy_quantity={}, electrical_energy_amount={})>"\
                .format(self.id, self.client_id, self.electrical_energy_quantity, self.electrical_energy_amount)
