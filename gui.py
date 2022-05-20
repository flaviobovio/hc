# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb  9 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pacientes", pos = wx.DefaultPosition, size = wx.Size( 800,580 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_bpButtonPrimero = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_2leftarrow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonPrimero.SetToolTipString( u"Primero" )
		
		bSizer9.Add( self.m_bpButtonPrimero, 0, wx.ALL, 5 )
		
		self.m_bpButtonAnterior = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_1leftarrow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonAnterior.SetToolTipString( u"Anterior" )
		
		bSizer9.Add( self.m_bpButtonAnterior, 0, wx.ALL, 5 )
		
		self.m_bpButtonSiguiente = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_player_play_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonSiguiente.SetToolTipString( u"Siguiente" )
		
		bSizer9.Add( self.m_bpButtonSiguiente, 0, wx.ALL, 5 )
		
		self.m_bpButtonUltimo = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_2rightarrow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonUltimo.SetToolTipString( u"Ultimo" )
		
		bSizer9.Add( self.m_bpButtonUltimo, 0, wx.ALL, 5 )
		
		self.m_bpButtonBuscar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_find_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonBuscar.SetToolTipString( u"Buscar" )
		
		bSizer9.Add( self.m_bpButtonBuscar, 0, wx.ALL, 5 )
		
		
		bSizer9.AddSpacer( ( 20, 0), 0, wx.EXPAND, 5 )
		
		self.m_bpButtonAgregar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_add_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonAgregar.SetToolTipString( u"Agregar" )
		
		bSizer9.Add( self.m_bpButtonAgregar, 0, wx.ALL, 5 )
		
		self.m_bpButtonEditar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonEditar.SetToolTipString( u"Editar" )
		
		bSizer9.Add( self.m_bpButtonEditar, 0, wx.ALL, 5 )
		
		self.m_bpButtonBorrar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_remove_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonBorrar.SetToolTipString( u"Borrar" )
		
		bSizer9.Add( self.m_bpButtonBorrar, 0, wx.ALL, 5 )
		
		self.m_bpButtonExportar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_filesystem_folder_yellow_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonExportar.SetToolTipString( u"Exportar Ficha Paciente" )
		
		bSizer9.Add( self.m_bpButtonExportar, 0, wx.ALL, 5 )
		
		
		bSizer9.AddSpacer( ( 20, 0), 0, wx.EXPAND, 5 )
		
		self.m_bpButtonGuardar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_apply_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonGuardar.SetToolTipString( u"Guardar" )
		
		bSizer9.Add( self.m_bpButtonGuardar, 0, wx.ALL, 5 )
		
		self.m_bpButtonDeshacer = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_reload_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonDeshacer.SetToolTipString( u"Deshacer" )
		
		bSizer9.Add( self.m_bpButtonDeshacer, 0, wx.ALL, 5 )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_bpButtonBackup = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_cdcopy_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonBackup.SetToolTipString( u"Respaldar Datos" )
		
		bSizer9.Add( self.m_bpButtonBackup, 0, wx.ALL, 5 )
		
		self.m_bpButtonCerrar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_exit_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonCerrar.SetToolTipString( u"Salir" )
		
		bSizer9.Add( self.m_bpButtonCerrar, 0, wx.ALL, 5 )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer9, 0, wx.EXPAND|wx.ALL, 5 )
		
		fgSizer7 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer7.Add( self.m_staticline11, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_staticText171 = wx.StaticText( self, wx.ID_ANY, u"Paciente", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText171.Wrap( -1 )
		self.m_staticText171.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText171.SetMinSize( wx.Size( 790,12 ) )
		
		fgSizer7.Add( self.m_staticText171, 0, wx.EXPAND|wx.LEFT, 5 )
		
		
		bSizer7.Add( fgSizer7, 1, wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 2, 5, 5, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetMinSize( wx.Size( 80,-1 ) )
		self.m_staticText7.SetMaxSize( wx.Size( 75,-1 ) )
		
		fgSizer2.Add( self.m_staticText7, 1, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.m_textCtrlId = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CAPITALIZE )
		self.m_textCtrlId.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlId, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP, 5 )
		
		
		fgSizer2.AddSpacer( ( 15, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetMinSize( wx.Size( 75,-1 ) )
		
		fgSizer2.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrlNombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlNombre.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlNombre, 1, wx.TOP, 5 )
		
		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Teléfono", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )
		fgSizer2.Add( self.m_staticText53, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlTelefono = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrlTelefono, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Dirección  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetMinSize( wx.Size( 75,-1 ) )
		
		fgSizer2.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlDireccion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlDireccion.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlDireccion, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Localidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer2.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrlLocalidad = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlLocalidad.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlLocalidad, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Provincia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer2.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrlProvincia = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlProvincia.SetMinSize( wx.Size( 150,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlProvincia, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Obra Social", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		fgSizer2.Add( self.m_staticText49, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlObra_Social = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlObra_Social.SetMinSize( wx.Size( 300,-1 ) )
		
		fgSizer2.Add( self.m_textCtrlObra_Social, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"F.Nacimiento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		fgSizer2.Add( self.m_staticText50, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.m_textCtrlFechaNacimiento = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrlFechaNacimiento, 0, 0, 5 )
		
		
		bSizer7.Add( fgSizer2, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer6 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Antecedentes\nFamiliares", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		self.m_staticText29.SetMinSize( wx.Size( 80,-1 ) )
		
		fgSizer6.Add( self.m_staticText29, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrlAntecedentes_Fam = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH2 )
		self.m_textCtrlAntecedentes_Fam.SetMinSize( wx.Size( 685,50 ) )
		
		fgSizer6.Add( self.m_textCtrlAntecedentes_Fam, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, u"Antecedentes\nPersonales", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		self.m_staticText48.SetMinSize( wx.Size( 80,50 ) )
		
		fgSizer6.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.m_textCtrlAntecedentes_Per = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH2 )
		self.m_textCtrlAntecedentes_Per.SetMinSize( wx.Size( 685,50 ) )
		
		fgSizer6.Add( self.m_textCtrlAntecedentes_Per, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		bSizer7.Add( fgSizer6, 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer7.Add( self.m_staticline1, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Visitas", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText17.Wrap( -1 )
		self.m_staticText17.SetMinSize( wx.Size( -1,12 ) )
		
		bSizer7.Add( self.m_staticText17, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		m_listBoxVisitasChoices = []
		self.m_listBoxVisitas = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxVisitasChoices, 0 )
		self.m_listBoxVisitas.SetMinSize( wx.Size( 200,160 ) )
		
		bSizer6.Add( self.m_listBoxVisitas, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		
		fgSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bpButton12 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_add_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer91.Add( self.m_bpButton12, 0, wx.ALL, 5 )
		
		self.m_bpButton13 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer91.Add( self.m_bpButton13, 0, wx.ALL, 5 )
		
		self.m_bpButton14 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_edit_remove_32.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer91.Add( self.m_bpButton14, 0, wx.ALL, 5 )
		
		
		fgSizer4.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer5 = wx.FlexGridSizer( 2, 5, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, u"Fecha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		fgSizer5.Add( self.m_staticText151, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_textCtrlFechaVisita = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrlFechaVisita, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		fgSizer5.AddSpacer( ( 20, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Motivo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer5.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlMotivo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlMotivo.SetMinSize( wx.Size( 340,-1 ) )
		
		fgSizer5.Add( self.m_textCtrlMotivo, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer8.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		self.m_textCtrlDetalle = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH2 )
		self.m_textCtrlDetalle.SetMinSize( wx.Size( 530,125 ) )
		
		bSizer8.Add( self.m_textCtrlDetalle, 0, wx.TOP|wx.BOTTOM, 5 )
		
		
		fgSizer4.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( fgSizer4, 0, wx.EXPAND, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer7.Add( self.m_staticline4, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		self.m_staticTextInfo = wx.StaticText( self, wx.ID_ANY, u" OMICRON SH       Belgrano 87       Venado Tuerto      TE 03462-435614       info@omicron-vt.com.ar       www.omicron-vt.com.ar", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextInfo.Wrap( -1 )
		bSizer7.Add( self.m_staticTextInfo, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		# Connect Events
		self.m_bpButtonPrimero.Bind( wx.EVT_BUTTON, self.m_OnButtonClickPrimero )
		self.m_bpButtonAnterior.Bind( wx.EVT_BUTTON, self.m_OnButtonClickAnterior )
		self.m_bpButtonSiguiente.Bind( wx.EVT_BUTTON, self.m_OnButtonClickSiguiente )
		self.m_bpButtonUltimo.Bind( wx.EVT_BUTTON, self.m_OnButtonClickUltimo )
		self.m_bpButtonBuscar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickBuscar )
		self.m_bpButtonAgregar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickAgregar )
		self.m_bpButtonEditar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickEditar )
		self.m_bpButtonBorrar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickBorrar )
		self.m_bpButtonExportar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickExportar )
		self.m_bpButtonGuardar.Bind( wx.EVT_BUTTON, self.m_OnButtonGuardar )
		self.m_bpButtonDeshacer.Bind( wx.EVT_BUTTON, self.m_OnButtonDeshacer )
		self.m_bpButtonBackup.Bind( wx.EVT_BUTTON, self.m_OnButtonBackup )
		self.m_bpButtonCerrar.Bind( wx.EVT_BUTTON, self.m_OnButtonCerrar )
		self.m_textCtrlId.Bind( wx.EVT_KILL_FOCUS, self.m_OnKillFocusCuenta )
		self.m_textCtrlFechaNacimiento.Bind( wx.EVT_CHAR, self.m_OnCharFechaNacimiento )
		self.m_textCtrlFechaNacimiento.Bind( wx.EVT_KILL_FOCUS, self.m_OnKillFocusFechaNacimiento )
		self.m_listBoxVisitas.Bind( wx.EVT_LISTBOX, self.m_OnListBoxVisitas )
		self.m_bpButton12.Bind( wx.EVT_BUTTON, self.m_OnButtonAgregarVisita )
		self.m_bpButton13.Bind( wx.EVT_BUTTON, self.m_OnButtonEditarVisita )
		self.m_bpButton14.Bind( wx.EVT_BUTTON, self.m_OnButtonBorrarVisita )
		self.m_textCtrlFechaVisita.Bind( wx.EVT_CHAR, self.m_OnCharFechaVisita )
		self.m_textCtrlFechaVisita.Bind( wx.EVT_KILL_FOCUS, self.m_OnKillFocusFechaVisita )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_OnButtonClickPrimero( self, event ):
		event.Skip()
	
	def m_OnButtonClickAnterior( self, event ):
		event.Skip()
	
	def m_OnButtonClickSiguiente( self, event ):
		event.Skip()
	
	def m_OnButtonClickUltimo( self, event ):
		event.Skip()
	
	def m_OnButtonClickBuscar( self, event ):
		event.Skip()
	
	def m_OnButtonClickAgregar( self, event ):
		event.Skip()
	
	def m_OnButtonClickEditar( self, event ):
		event.Skip()
	
	def m_OnButtonClickBorrar( self, event ):
		event.Skip()
	
	def m_OnButtonClickExportar( self, event ):
		event.Skip()
	
	def m_OnButtonGuardar( self, event ):
		event.Skip()
	
	def m_OnButtonDeshacer( self, event ):
		event.Skip()
	
	def m_OnButtonBackup( self, event ):
		event.Skip()
	
	def m_OnButtonCerrar( self, event ):
		event.Skip()
	
	def m_OnKillFocusCuenta( self, event ):
		event.Skip()
	
	def m_OnCharFechaNacimiento( self, event ):
		event.Skip()
	
	def m_OnKillFocusFechaNacimiento( self, event ):
		event.Skip()
	
	def m_OnListBoxVisitas( self, event ):
		event.Skip()
	
	def m_OnButtonAgregarVisita( self, event ):
		event.Skip()
	
	def m_OnButtonEditarVisita( self, event ):
		event.Skip()
	
	def m_OnButtonBorrarVisita( self, event ):
		event.Skip()
	
	def m_OnCharFechaVisita( self, event ):
		event.Skip()
	
	def m_OnKillFocusFechaVisita( self, event ):
		event.Skip()
	

###########################################################################
## Class BuscarDialog
###########################################################################

class BuscarDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Buscar por", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		fgSizer3.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBoxCamposChoices = []
		self.m_comboBoxCampos = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBoxCamposChoices, wx.CB_READONLY|wx.CB_SIMPLE )
		self.m_comboBoxCampos.SetMinSize( wx.Size( 250,-1 ) )
		
		fgSizer3.Add( self.m_comboBoxCampos, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlCadena = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlCadena.SetMinSize( wx.Size( 330,-1 ) )
		
		fgSizer3.Add( self.m_textCtrlCadena, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_bpButtonBuscar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"iconos/Crystal_Clear_action_find_16.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer3.Add( self.m_bpButtonBuscar, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( fgSizer3, 0, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticTextEncabezado = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextEncabezado.Wrap( -1 )
		self.m_staticTextEncabezado.SetFont( wx.Font( 8, 76, 90, 92, False, "Droid Sans Mono" ) )
		
		bSizer8.Add( self.m_staticTextEncabezado, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		m_listBoxResultadosChoices = []
		self.m_listBoxResultados = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxResultadosChoices, 0 )
		self.m_listBoxResultados.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Droid Sans Mono" ) )
		self.m_listBoxResultados.SetMinSize( wx.Size( 700,400 ) )
		
		bSizer8.Add( self.m_listBoxResultados, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer7.Add( bSizer9, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_textCtrlCadena.Bind( wx.EVT_KEY_DOWN, self.m_OnKeyDownCadena )
		self.m_bpButtonBuscar.Bind( wx.EVT_BUTTON, self.m_OnButtonClickBuscar )
		self.m_listBoxResultados.Bind( wx.EVT_KEY_DOWN, self.m_OnKeyDownResultados )
		self.m_listBoxResultados.Bind( wx.EVT_LEFT_DCLICK, self.m_OnLeftClickResultados )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_OnKeyDownCadena( self, event ):
		event.Skip()
	
	def m_OnButtonClickBuscar( self, event ):
		event.Skip()
	
	def m_OnKeyDownResultados( self, event ):
		event.Skip()
	
	def m_OnLeftClickResultados( self, event ):
		event.Skip()
	

