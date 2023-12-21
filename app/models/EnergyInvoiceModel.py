import uuid
from sqlalchemy import func, Column, Integer, Float, String, TIMESTAMP
from sqlalchemy_utils import UUIDType

from config.DataBaseManager import Base

class EnergyInvoiceModel(Base):
    __tablename__ = "invoices"

    id = Column(
        UUIDType(binary=False), 
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    
    client_id = Column(
        String,
        index=True
    )
    
    reference_month = Column(
        String, 
        index=True
    )
    
    electrical_energy_amount = Column(
        Float
    )

    electrical_energy_value = Column(
        Float
    )

    electrical_energy_scee_amount = Column(
        Float
    )

    electrical_energy_scee_value = Column(
        Float
    )

    electrical_energy_gdi_amount = Column(
        Float
    )

    electrical_energy_gdi_value = Column(
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

    def __repr__(self):
        return "<Book(id='{}', client_id='{}', electrical_energy_amount={}, electrical_energy_value={})>"\
                .format(self.id, self.client_id, self.electrical_energy_amount, self.electrical_energy_value)
