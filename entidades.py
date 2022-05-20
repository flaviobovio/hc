from sqlalchemy import *
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


BASE = declarative_base()
DATABASE = create_engine('sqlite:///database.db')
DATABASE.echo = False
METADATA = MetaData(DATABASE)
SESSIONCLASS = sessionmaker(bind=DATABASE)
SESSION = SESSIONCLASS()






class Paciente(BASE):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(VARCHAR(50))
    direccion = Column(VARCHAR(50))
    localidad = Column(VARCHAR(50))
    provincia = Column(VARCHAR(20))
    telefono = Column(VARCHAR(50))
    obra_social = Column(VARCHAR(50))
    fecha_nacimiento = Column(Date)    
    antecedentes_fam = Column(TEXT)
    antecedentes_per = Column(TEXT)
    visitas = relationship("Visita", order_by="desc(Visita.fecha)", backref="Paciente")   


    def __init__(self, nombre, direccion, localidad, provincia, telefono, obra_social, fecha_nacimiento,\
                antecedentes_fam, antecedentes_per):
        self.nombre = nombre
        self.direccion = direccion
        self.localidad = localidad
        self.provincia = provincia
        self.telefono = telefono 
        self.obra_social = obra_social
        self.fecha_nacimiento = fecha_nacimiento
        self.antecedentes_fam = antecedentes_fam
        self.antecedentes_per = antecedentes_per

    def __repr__(self):
            return "<Paciente('%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.nombre, self.direccion, self.localidad,\
            self.provincia,self.telefono,self.obra_social,self.fecha_nacimiento, self.antecedentes_fam, self.antecedentes_per)
            
            
class Visita(BASE):
    __tablename__ = 'visitas'
    id = Column(Integer, primary_key=True)
    id_paciente = Column(Integer, ForeignKey('pacientes.id'))      
    fecha = Column(Date)
    motivo = Column(VARCHAR(50))
    detalle = Column(TEXT)
    paciente = relationship("Paciente")

    def __init__(self, id_paciente, fecha, motivo, detalle):
        self.id_paciente = id_paciente
        self.fecha = fecha
        self.motivo = motivo
        self.detalle = detalle
    def __repr__(self):
        return "<Visita('%s','%s','%s','%s')>" % (self.id_paciente, self.fecha, self.motivo, self.detalle)
   

#       Crear Tablas
BASE.metadata.create_all(DATABASE) 
