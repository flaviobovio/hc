import wx
import gui
from entidades import *
import datetime
from time import time
from Validadores import *
from BuscarPacienteDialog import BuscarPacienteDialog
from datetime import date
from Funciones import *



class PacientePanel ( gui.PacientePanelBase ):
    
    m_Paciente = None

 
    def __init__( self, parent ):
        gui.PacientePanelBase.__init__( self, parent )
        self.HabilitarControles(False)  

    
    def LlenarControles (self):       
        if self.m_Paciente.id == None:           
            self.m_textCtrlId.SetValue("")    
            self.m_datePickerFecha_Nacimiento.SetValue(FechaDatePicker(date(1900, 1, 1)))
        else:
            self.m_textCtrlId.SetValue(str(self.m_Paciente.id))
            self.m_textCtrlNombre.SetValue(self.m_Paciente.nombre)
            self.m_textCtrlDireccion.SetValue(self.m_Paciente.direccion)
            self.m_textCtrlLocalidad.SetValue(self.m_Paciente.localidad)
            self.m_textCtrlProvincia.SetValue(self.m_Paciente.provincia)
            self.m_textCtrlTelefono.SetValue(self.m_Paciente.telefono)
            self.m_textCtrlObra_Social.SetValue(self.m_Paciente.obra_social)
            self.m_textCtrlAntecedentes_Fam.SetValue(self.m_Paciente.antecedentes_fam)
            self.m_textCtrlAntecedentes_Per.SetValue(self.m_Paciente.antecedentes_per)                
            self.m_datePickerFecha_Nacimiento.SetValue(FechaDatePicker(self.m_Paciente.fecha_nacimiento))


        
    def VaciarDatos (self):
        self.m_Paciente = Paciente ("", "", "", "", "", "", None, "", "")
        self.LlenarControles()

    def HabilitarControles(self, acti): # True Activar, False Desactivar
        for ctrl in self.GetChildren():
            if ctrl.GetName() != "button":
                ctrl.Enable(acti)
                #ctrl.SetBackgroundColour ('WHITE')
                if acti:
                    ctrl.SetForegroundColour ('DARK_GREY')
                else:
                    ctrl.SetForegroundColour ('GREY')                
            else:
                ctrl.Enable(not acti)
        self.m_textCtrlId.Enable(False)
        self.m_bpButtonDeshacer.Enable(acti)
        self.m_bpButtonGuardar.Enable(acti)       
        self.m_textCtrlNombre.SetFocus()
      

    
    def m_OnButtonClickPrimero( self, event ):  
        self.m_Paciente = SESSION.query(Paciente).order_by(Paciente.id).first()
        self.LlenarControles()
    def m_OnButtonClickAnterior( self, event ):
        cuen = self.m_textCtrlId.GetValue()
        self.m_Paciente = SESSION.query(Paciente).order_by(desc(Paciente.id)).filter(Paciente.id < cuen).first()
        if self.m_Paciente != None:
            self.LlenarControles()
    
    def m_OnButtonClickSiguiente( self, event ):
        cuen = self.m_textCtrlId.GetValue()
        self.m_Paciente = SESSION.query(Paciente).order_by(Paciente.id).filter(Paciente.id > cuen).first()
       
        if self.m_Paciente != None:
            self.LlenarControles()
    
    def m_OnButtonClickUltimo( self, event ):
        self.m_Paciente = SESSION.query(Paciente).order_by(desc(Paciente.id)).first()
        self.LlenarControles()

    def m_OnButtonClickAgregar( self, event ):
        self.VaciarDatos()
        self.HabilitarControles(True)
    
    def m_OnButtonClickEditar( self, event ):
        if self.m_Paciente != None:
            self.HabilitarControles(True)
    
    def m_OnButtonClickBorrar( self, event ):
        if self.m_Paciente != None:
            acep = wx.MessageBox("Borrar Paciente ?", "Confirma", wx.YES_NO)
            if (acep == wx.YES):
                SESSION.delete(self.m_Paciente)
                SESSION.commit()
                self.VaciarDatos()
                

            
    def m_OnButtonGuardar( self, event ):
        if self.Validate():
            self.m_Paciente.nombre           = self.m_textCtrlNombre.GetValue()
            self.m_Paciente.direccion        = self.m_textCtrlDireccion.GetValue()
            self.m_Paciente.localidad        = self.m_textCtrlLocalidad.GetValue()
            self.m_Paciente.provincia        = self.m_textCtrlProvincia.GetValue()
            self.m_Paciente.telefono         = self.m_textCtrlTelefono.GetValue()
            self.m_Paciente.obra_social      = self.m_textCtrlObra_Social.GetValue()
            self.m_Paciente.antecedentes_fam = self.m_textCtrlAntecedentes_Fam.GetValue()
            self.m_Paciente.antecedentes_per = self.m_textCtrlAntecedentes_Per.GetValue()  
            self.m_Paciente.fecha_nacimiento = DatePickerFecha(self.m_datePickerFecha_Nacimiento.GetValue())

            SESSION.merge(self.m_Paciente)
            SESSION.commit()
            self.HabilitarControles(False)            
        else:
            wx.MessageBox("Ingrese correctamenta los campos requeridos", "Error")
        

    
    def m_OnButtonDeshacer( self, event ):
        self.m_Paciente = None
        self.VaciarDatos()
        self.HabilitarControles(False)
        
    def m_OnButtonClickBuscar( self, event ):
        busDialog = BuscarPacienteDialog(self) 
        busDialog.ShowModal()
        self.LlenarControles()
