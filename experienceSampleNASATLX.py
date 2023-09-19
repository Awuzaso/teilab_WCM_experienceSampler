# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-294-gf1343abd)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class nasaTLXDialog
###########################################################################

class nasaTLXDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 490,694 ), style = wx.CLOSE_BOX|wx.DIALOG_NO_PARENT|wx.HSCROLL|wx.VSCROLL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		nasaTLX_Sizer = wx.BoxSizer( wx.VERTICAL )

		self.tlxIntroduction = wx.StaticText( self, wx.ID_ANY, u"Below are a series of scales that will ask you to rate how your task for today  was in accordance to various demands listed below. Please record your response on the 21 grade scale.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlxIntroduction.Wrap( 450 )

		nasaTLX_Sizer.Add( self.tlxIntroduction, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlxScale = wx.StaticText( self, wx.ID_ANY, u"0 = Very Low, 21 = Very High", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlxScale.Wrap( -1 )

		nasaTLX_Sizer.Add( self.tlxScale, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		nasaTLX_Sizer.Add( ( 0, 0), 1, 0, 5 )

		tlx_mental_demand_sizer = wx.BoxSizer( wx.VERTICAL )

		self.tlx_mental_demand_title = wx.StaticText( self, wx.ID_ANY, u"Mental Demand", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlx_mental_demand_title.Wrap( -1 )

		tlx_mental_demand_sizer.Add( self.tlx_mental_demand_title, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlx_mental_demand_question = wx.StaticText( self, wx.ID_ANY, u"How mentally demanding was the task?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlx_mental_demand_question.Wrap( -1 )

		tlx_mental_demand_sizer.Add( self.tlx_mental_demand_question, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlx_mental_demand_slider = wx.Slider( self, wx.ID_ANY, 0, 0, 21, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		tlx_mental_demand_sizer.Add( self.tlx_mental_demand_slider, 0, wx.EXPAND, 5 )


		nasaTLX_Sizer.Add( tlx_mental_demand_sizer, 0, wx.EXPAND, 5 )

		tlx_phys_demand_sizer = wx.BoxSizer( wx.VERTICAL )

		self.tlx_phys_demand_title = wx.StaticText( self, wx.ID_ANY, u"Physical Demand", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlx_phys_demand_title.Wrap( -1 )

		tlx_phys_demand_sizer.Add( self.tlx_phys_demand_title, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlx_phys_demand_question = wx.StaticText( self, wx.ID_ANY, u"How physically demanding was the task?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlx_phys_demand_question.Wrap( -1 )

		tlx_phys_demand_sizer.Add( self.tlx_phys_demand_question, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlx_phys_demand_question = wx.Slider( self, wx.ID_ANY, 0, 0, 21, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		tlx_phys_demand_sizer.Add( self.tlx_phys_demand_question, 0, wx.EXPAND, 5 )


		nasaTLX_Sizer.Add( tlx_phys_demand_sizer, 0, wx.EXPAND, 5 )

		tlx_temp_demand_sizer = wx.BoxSizer( wx.VERTICAL )

		self.tlx_temp_demand_title = wx.StaticText( self, wx.ID_ANY, u"Temporal Demand", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlx_temp_demand_title.Wrap( -1 )

		tlx_temp_demand_sizer.Add( self.tlx_temp_demand_title, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlx_temp_demand_question = wx.StaticText( self, wx.ID_ANY, u"How hurried or rushed was the pace of the task?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlx_temp_demand_question.Wrap( -1 )

		tlx_temp_demand_sizer.Add( self.tlx_temp_demand_question, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlx_temp_demand_slider = wx.Slider( self, wx.ID_ANY, 0, 0, 21, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		tlx_temp_demand_sizer.Add( self.tlx_temp_demand_slider, 0, wx.EXPAND, 5 )


		nasaTLX_Sizer.Add( tlx_temp_demand_sizer, 0, wx.EXPAND, 5 )

		tlx_perf_demand_sizer = wx.BoxSizer( wx.VERTICAL )

		self.tlx_perf_demand_title = wx.StaticText( self, wx.ID_ANY, u"Performance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlx_perf_demand_title.Wrap( -1 )

		tlx_perf_demand_sizer.Add( self.tlx_perf_demand_title, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlx_perf_demand_question = wx.StaticText( self, wx.ID_ANY, u"How successful were you in accomplishing what you were asked to do?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlx_perf_demand_question.Wrap( -1 )

		tlx_perf_demand_sizer.Add( self.tlx_perf_demand_question, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlx_perf_demand_slider = wx.Slider( self, wx.ID_ANY, 0, 0, 21, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		tlx_perf_demand_sizer.Add( self.tlx_perf_demand_slider, 0, wx.EXPAND, 5 )


		nasaTLX_Sizer.Add( tlx_perf_demand_sizer, 0, wx.EXPAND, 5 )

		tlx_effort_demand_sizer = wx.BoxSizer( wx.VERTICAL )

		self.tlx_effort_demand_title = wx.StaticText( self, wx.ID_ANY, u"Effort", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlx_effort_demand_title.Wrap( -1 )

		tlx_effort_demand_sizer.Add( self.tlx_effort_demand_title, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlx_effort_demand_question = wx.StaticText( self, wx.ID_ANY, u"How hard did you have to work to accomplish your level of performance?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlx_effort_demand_question.Wrap( -1 )

		tlx_effort_demand_sizer.Add( self.tlx_effort_demand_question, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlx_effort_demand_slider = wx.Slider( self, wx.ID_ANY, 0, 0, 21, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		tlx_effort_demand_sizer.Add( self.tlx_effort_demand_slider, 0, wx.EXPAND, 5 )


		nasaTLX_Sizer.Add( tlx_effort_demand_sizer, 0, wx.EXPAND, 5 )

		tlx_frustration_demand_sizer = wx.BoxSizer( wx.VERTICAL )

		self.tlx_frustration_demand_title = wx.StaticText( self, wx.ID_ANY, u"Frustration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlx_frustration_demand_title.Wrap( -1 )

		tlx_frustration_demand_sizer.Add( self.tlx_frustration_demand_title, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlx_frustration_demand_question = wx.StaticText( self, wx.ID_ANY, u"How mentally demanding was the task?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tlx_frustration_demand_question.Wrap( -1 )

		tlx_frustration_demand_sizer.Add( self.tlx_frustration_demand_question, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tlx_frustration_demand_question = wx.Slider( self, wx.ID_ANY, 0, 0, 21, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_LABELS )
		tlx_frustration_demand_sizer.Add( self.tlx_frustration_demand_question, 0, wx.EXPAND, 5 )


		nasaTLX_Sizer.Add( tlx_frustration_demand_sizer, 1, wx.EXPAND, 5 )


		nasaTLX_Sizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.tlx_comment = wx.TextCtrl( self, wx.ID_ANY, u"Write any comment here.", wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE )
		nasaTLX_Sizer.Add( self.tlx_comment, 1, wx.ALL|wx.EXPAND, 5 )

		self.tlx_submit_button = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		nasaTLX_Sizer.Add( self.tlx_submit_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( nasaTLX_Sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tlx_mental_demand_slider.Bind( wx.EVT_SCROLL, self.mentalDemandScroll )
		self.tlx_phys_demand_question.Bind( wx.EVT_SCROLL, self.physDemandScroll )
		self.tlx_temp_demand_slider.Bind( wx.EVT_SCROLL, self.tempDemandScroll )
		self.tlx_perf_demand_slider.Bind( wx.EVT_SCROLL, self.perfDemandScroll )
		self.tlx_effort_demand_slider.Bind( wx.EVT_SCROLL, self.effortScroll )
		self.tlx_frustration_demand_question.Bind( wx.EVT_SCROLL, self.frustrationScroll )
		self.tlx_submit_button.Bind( wx.EVT_BUTTON, self.onSubmit )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def mentalDemandScroll( self, event ):
		event.Skip()

	def physDemandScroll( self, event ):
		event.Skip()

	def tempDemandScroll( self, event ):
		event.Skip()

	def perfDemandScroll( self, event ):
		event.Skip()

	def effortScroll( self, event ):
		event.Skip()

	def frustrationScroll( self, event ):
		event.Skip()

	def onSubmit( self, event ):
		event.Skip()


###########################################################################
## Class surveyRequestWindow
###########################################################################

class surveyRequestWindow ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 462,148 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		surveyRequestWindowSizer = wx.BoxSizer( wx.VERTICAL )

		self.surveyRequestWindowLabel = wx.StaticText( self, wx.ID_ANY, u"Do you have time to complete a quick survey on your current work context switching activities?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.surveyRequestWindowLabel.Wrap( 448 )

		surveyRequestWindowSizer.Add( self.surveyRequestWindowLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		surveyRequestWindowSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		surveyRequestWindowAnswerSizer = wx.GridSizer( 0, 2, 0, 0 )

		self.surveyRequestWindowAnswerButtonYes = wx.Button( self, wx.ID_ANY, u"Yes", wx.DefaultPosition, wx.DefaultSize, 0 )
		surveyRequestWindowAnswerSizer.Add( self.surveyRequestWindowAnswerButtonYes, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.surveyRequestWindowAnswerButtonNo = wx.Button( self, wx.ID_ANY, u"No", wx.DefaultPosition, wx.DefaultSize, 0 )
		surveyRequestWindowAnswerSizer.Add( self.surveyRequestWindowAnswerButtonNo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		surveyRequestWindowSizer.Add( surveyRequestWindowAnswerSizer, 1, wx.EXPAND, 5 )


		self.SetSizer( surveyRequestWindowSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.closeFunc )
		self.surveyRequestWindowAnswerButtonYes.Bind( wx.EVT_BUTTON, self.onClickYesButton )
		self.surveyRequestWindowAnswerButtonNo.Bind( wx.EVT_BUTTON, self.onClickNoButton )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def closeFunc( self, event ):
		event.Skip()

	def onClickYesButton( self, event ):
		event.Skip()

	def onClickNoButton( self, event ):
		event.Skip()


###########################################################################
## Class wcmEthnographyApp
###########################################################################

class wcmEthnographyApp ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Work Context Management Ethnography Study ", pos = wx.DefaultPosition, size = wx.Size( 500,228 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		wcmEthnographyAppSizer = wx.BoxSizer( wx.VERTICAL )

		wcmEthnographyAppGridSizer = wx.GridSizer( 2, 2, 0, 0 )

		self.wcmEthnographyAppSwitchButton = wx.Button( self, wx.ID_ANY, u"I switched", wx.DefaultPosition, wx.DefaultSize, 0 )
		wcmEthnographyAppGridSizer.Add( self.wcmEthnographyAppSwitchButton, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.wcmEthnographyAppEODbutton = wx.Button( self, wx.ID_ANY, u"End-of-Day Survey", wx.DefaultPosition, wx.DefaultSize, 0 )
		wcmEthnographyAppGridSizer.Add( self.wcmEthnographyAppEODbutton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.wcmEthnographyAppCheckBox = wx.CheckBox( self, wx.ID_ANY, u"Record?", wx.DefaultPosition, wx.DefaultSize, 0 )
		wcmEthnographyAppGridSizer.Add( self.wcmEthnographyAppCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.wcmEthnographyRecordFolder = wx.Button( self, wx.ID_ANY, u"Go to my recordings/data", wx.DefaultPosition, wx.DefaultSize, 0 )
		wcmEthnographyAppGridSizer.Add( self.wcmEthnographyRecordFolder, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		wcmEthnographyAppSizer.Add( wcmEthnographyAppGridSizer, 1, wx.EXPAND, 5 )


		self.SetSizer( wcmEthnographyAppSizer )
		self.Layout()
		self.menuBarMain = wx.MenuBar( 0 )
		self.menuFileMainGroup = wx.Menu()
		self.menuFileQuit = wx.MenuItem( self.menuFileMainGroup, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFileMainGroup.Append( self.menuFileQuit )

		self.menuBarMain.Append( self.menuFileMainGroup, u"WCM-Eth-App" )

		self.helpMenu = wx.Menu()
		self.helpMenuAbout = wx.MenuItem( self.helpMenu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.helpMenu.Append( self.helpMenuAbout )

		self.menuBarMain.Append( self.helpMenu, u"Help" )

		self.SetMenuBar( self.menuBarMain )


		self.Centre( wx.BOTH )

		# Connect Events
		self.wcmEthnographyAppSwitchButton.Bind( wx.EVT_BUTTON, self.onSwitchButtonClick )
		self.wcmEthnographyAppEODbutton.Bind( wx.EVT_BUTTON, self.eodSurveyClick )
		self.wcmEthnographyAppCheckBox.Bind( wx.EVT_CHECKBOX, self.onRecordCheck )
		self.wcmEthnographyRecordFolder.Bind( wx.EVT_BUTTON, self.onGoToRecordData )
		self.Bind( wx.EVT_MENU, self.onMenuQuit, id = self.menuFileQuit.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def onSwitchButtonClick( self, event ):
		event.Skip()

	def eodSurveyClick( self, event ):
		event.Skip()

	def onRecordCheck( self, event ):
		event.Skip()

	def onGoToRecordData( self, event ):
		event.Skip()

	def onMenuQuit( self, event ):
		event.Skip()


###########################################################################
## Class EODvideoSurveyDialog
###########################################################################

class EODvideoSurveyDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"End-of-Day Video Survey", pos = wx.DefaultPosition, size = wx.Size( 462,375 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		eodSizer = wx.BoxSizer( wx.VERTICAL )

		eodCurrentVideoSizer = wx.BoxSizer( wx.VERTICAL )

		self.eodCurrentVideoText = wx.StaticText( self, wx.ID_ANY, u"Current Video:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.eodCurrentVideoText.Wrap( -1 )

		eodCurrentVideoSizer.Add( self.eodCurrentVideoText, 0, wx.ALL, 5 )

		self.currentVideoLabelText = wx.StaticText( self, wx.ID_ANY, u"No video is displayed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.currentVideoLabelText.Wrap( -1 )

		eodCurrentVideoSizer.Add( self.currentVideoLabelText, 0, wx.ALL, 5 )


		eodSizer.Add( eodCurrentVideoSizer, 1, wx.EXPAND, 5 )

		eodVideoSwitchSizer = wx.GridSizer( 0, 3, 0, 0 )

		self.eodVideoSwitchPrev = wx.Button( self, wx.ID_ANY, u"Previous Video", wx.DefaultPosition, wx.DefaultSize, 0 )
		eodVideoSwitchSizer.Add( self.eodVideoSwitchPrev, 0, wx.ALL, 5 )

		self.eodVideoSwitchWatchVideo = wx.Button( self, wx.ID_ANY, u"Watch video", wx.DefaultPosition, wx.DefaultSize, 0 )
		eodVideoSwitchSizer.Add( self.eodVideoSwitchWatchVideo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.eodVideoSwitchNext = wx.Button( self, wx.ID_ANY, u"Next Video", wx.DefaultPosition, wx.DefaultSize, 0 )
		eodVideoSwitchSizer.Add( self.eodVideoSwitchNext, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		eodSizer.Add( eodVideoSwitchSizer, 1, wx.EXPAND, 5 )

		self.eodSwitchTextInstruction = wx.StaticText( self, wx.ID_ANY, u"Please press the “Watch Video” button to view the current video snippet. Provide context as to what you were doing at the time, how your personal computer and physical resources helped or made it difficult for you to switch between different projects.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.eodSwitchTextInstruction.Wrap( 450 )

		eodSizer.Add( self.eodSwitchTextInstruction, 0, wx.ALL, 5 )

		self.eodControlNote = wx.TextCtrl( self, wx.ID_ANY, u"Write comments here.", wx.DefaultPosition, wx.DefaultSize, 0 )
		eodSizer.Add( self.eodControlNote, 1, wx.ALL|wx.EXPAND, 5 )

		self.surveySubmissionButton = wx.Button( self, wx.ID_ANY, u"Submit end of day survey", wx.DefaultPosition, wx.DefaultSize, 0 )
		eodSizer.Add( self.surveySubmissionButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( eodSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.eodVideoSwitchPrev.Bind( wx.EVT_BUTTON, self.onSwitchPrev )
		self.eodVideoSwitchWatchVideo.Bind( wx.EVT_BUTTON, self.onWatchVideo )
		self.eodVideoSwitchNext.Bind( wx.EVT_BUTTON, self.onSwitchNext )
		self.surveySubmissionButton.Bind( wx.EVT_BUTTON, self.onSubmit )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def onSwitchPrev( self, event ):
		event.Skip()

	def onWatchVideo( self, event ):
		event.Skip()

	def onSwitchNext( self, event ):
		event.Skip()

	def onSubmit( self, event ):
		event.Skip()


