import wx 
  
#import the newly created GUI file 
import experienceSampleNASATLX  
class testFrame(experienceSampleNASATLX.MyDialog4): 
   def __init__(self,parent): 
      Demo.MyFrame1.__init__(self,parent)  
		
   def FindSquare(self,event): 
      num = int(self.m_textCtrl1.GetValue()) 
      self.m_textCtrl5.SetValue (str(num*num)) 
        
app = wx.App(False) 
frame = testFrame(None) 
frame.Show(True) 
#start the applications 
app.MainLoop() 