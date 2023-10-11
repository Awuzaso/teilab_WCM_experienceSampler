import os
import platform
import subprocess
import threading
import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab
import wx 
import numpy
import csv

from datetime import datetime
from os.path import exists

    
#import the newly created GUI file. GUI
# file is created interactively in wxformbuilder:
# https://github.com/wxFormBuilder/wxFormBuilder 
import experienceSampleNASATLX



#https://stackoverflow.com/questions/6631299/python-opening-a-folder-in-explorer-nautilus-finder

'''
/////////////////////////////////////////////////////////////////
////// Utility Functions            /////////////////////////////
/////////////////////////////////////////////////////////////////
'''


'''
Note: Somewhat related, I would like for this applicaiton to be an
executable so we can avoid having to install libraries for the
participants.
'''

def getDateTime():
    # datetime object containing current date and time
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S_")
    return dt_string


def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def writeToCSV(filePath,header,data):
    with open(filePath, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)

def appendToCSV(filePath,header,data):
    with open(filePath, 'a', encoding='UTF8', newline='') as fd:
        writer = csv.writer(fd)
        writer.writerow(header)
        writer.writerows(data)



'''
/////////////////////////////////////////////////////////////////
////// End-of-Day (EoD) Survey (WIP) Window Class     //////////////////////
Note: Intent behind this window class is to implement an auto-
generated survey that collects the video snapshots throughtout the day
for retrospective survey on the participants' own working context
practices throughout the work day.
/////////////////////////////////////////////////////////////////
'''

class eodSurvey(experienceSampleNASATLX.EODvideoSurveyDialog):
    
    listOfVideos = []
    currentSelectedVideo = ""
    indexOfVideo = 0
    videoSurveyData = [[],[]]

    def getListOfVideos(self):
        path = '../wcmEthRecData'
        files = os.listdir(path)

        for f in os.listdir(path):
            name,ext = os.path.splitext(f)
            if ext == '.mp4':
                videoFile = name+ext
                self.listOfVideos.append(videoFile)



        #self.listOfVideos = files
        print(self.listOfVideos)
        self.currentSelectedVideo = self.listOfVideos[0]
        for f in self.listOfVideos:
            print(f)

    def __init__(self, parent, title):
        experienceSampleNASATLX.EODvideoSurveyDialog.__init__(self,parent)
        self.getListOfVideos()
        self.videoSurveyData = [[" "," "]] * len(self.listOfVideos)
        print(self.videoSurveyData)
        self.surveySubmissionButton.Disable()
        self.currentVideoLabelText.SetLabel(self.currentSelectedVideo)
        # Update frame
        self.GetParent().Layout()


    def onWatchVideo(self,event):
        print("Video opened!")
        open_file("/Users/awuzaso/Documents/wcmEthRecData/"+self.currentSelectedVideo)
##################

###FIX THE TRAVERSAL

#################
    def onSwitchPrev(self,event):
        print("Eod prev switch button pressed!")
        if(self.indexOfVideo > 0):
            self.videoSurveyData[[self.indexOfVideo][0]] = self.listOfVideos[self.indexOfVideo]
            self.videoSurveyData[[self.indexOfVideo][1]] = self.eodControlNote.GetValue()
            self.indexOfVideo = self.indexOfVideo - 1
            self.currentVideoLabelText.SetLabel(self.listOfVideos[self.indexOfVideo])
            self.GetParent().Layout()
            

    def onSwitchNext(self,event):
        print("Eod next switch button pressed!")
        if(self.indexOfVideo < len(self.listOfVideos)-1):
            self.videoSurveyData[[self.indexOfVideo][0]] = self.listOfVideos[self.indexOfVideo]
            self.videoSurveyData[[self.indexOfVideo][1]] = self.eodControlNote.GetValue()
            self.indexOfVideo = self.indexOfVideo + 1
            self.currentVideoLabelText.SetLabel(self.listOfVideos[self.indexOfVideo])
            self.GetParent().Layout()
            if(self.indexOfVideo == len(self.listOfVideos)-1):
                self.surveySubmissionButton.Enable()
                self.GetParent().Layout()
            if(self.indexOfVideo < len(self.listOfVideos)-1 ):
                self.surveySubmissionButton.Disable()
                self.GetParent().Layout()

    def onSubmit(self,event):
        print("On submit button was pressed.")
        print(self.videoSurveyData)

 
'''
/////////////////////////////////////////////////////////////////
////// NASA-TLX Modal Window Class      //////////////////////
Note: Modal window of 7 item NASA-TLX instrument. Functional but
file path is hardcoded to the original development environment.
Modal window is launched when the participant clicks "Yes" from
"surveyRequestDialog(...)". "Yes" is connected to 
"onClickYesButton(self,event)""
FYI: https://humansystems.arc.nasa.gov/groups/tlx/

/////////////////////////////////////////////////////////////////
'''           

class nasaTLXWindow(experienceSampleNASATLX.nasaTLXDialog):

    mentalDemandVal = 0
    physDemandVal = 0
    tempDemandVal = 0
    performanceVal = 0
    effortVal = 0
    frustrationVal = 0
    textNoteVal = " "


    def __init__(self, parent, title):
        experienceSampleNASATLX.nasaTLXDialog.__init__(self,parent)

    def closeWindowFunc(self):
        lst = wx.GetTopLevelWindows()
        lst[2].Destroy()
        lst[1].Destroy()
        lst2 = wx.GetTopLevelWindows()
        print(lst2)
        # lst[1].Hide()
        # self.Destroy()


    def onSubmit(self,event):

        self.textNoteVal = self.tlx_comment.GetValue()

        # Needs to be changed so that its not hard coded for the path
        filePath = "/Users/awuzaso/Documents/wcmEthRecData/tlxData/"
        file_exists = exists(filePath)

        if(file_exists == False):
            print("File does not exist!")
            os.mkdir(filePath)
            header = ['Mental Demand:', "Physical Demand:", "Temporal Demand:", "Performance Demand:", "Effort:", "Frustration", "Note"]

            data = [[self.mentalDemandVal, self.physDemandVal, self.tempDemandVal, self.performanceVal, self.effortVal, self.frustrationVal, self.textNoteVal]]

            filePathName = filePath + getDateTime() + "nasaTLXData.csv"

            writeToCSV(filePathName,header,data)

        else:
            header = ['Mental Demand:', "Physical Demand:", "Temporal Demand:", "Performance Demand:", "Effort:", "Frustration", "Note"]

            data = [[self.mentalDemandVal, self.physDemandVal, self.tempDemandVal, self.performanceVal, self.effortVal, self.frustrationVal, self.textNoteVal]]

            filePathName = filePath + getDateTime() + "nasaTLXData.csv"

            writeToCSV(filePathName,header,data)


        ''''
        !!!!!!!!!!!!!!!!!!!!!!!
        '''

        self.closeWindowFunc()

    def mentalDemandScroll(self,e):
        obj = e.GetEventObject()
        self.mentalDemandVal = obj.GetValue()
        

    def physDemandScroll(self,e):
        obj = e.GetEventObject()
        self.physDemandVal = obj.GetValue()

    def tempDemandScroll(self,e):
        obj = e.GetEventObject()
        self.tempDemandVal = obj.GetValue()

    def perfDemandScroll(self,e):
        obj = e.GetEventObject()
        self.performanceVal = obj.GetValue()

    def effortScroll(self,e):
        obj = e.GetEventObject()
        self.effortVal = obj.GetValue()

    def frustrationScroll(self,e):
        obj = e.GetEventObject()
        self.frustrationVal = obj.GetValue()

'''
/////////////////////////////////////////////////////////////////
////// surveyRequestDialog (WIP)               //////////////////////
Note: Dialog window that asks participants if they are able to
complete NASA-TLX survey when prompted by the application. Class 
function, "onClickYesButton(self,event)", is currently hardcoded for
its save directory. This needs to be changed so that this can be defined
by the user.
/////////////////////////////////////////////////////////////////
''' 
class surveyRequestDialog(experienceSampleNASATLX.surveyRequestWindow): 
     def __init__(self, parent, title):
        experienceSampleNASATLX.surveyRequestWindow.__init__(self,parent)

     def closeFunc(self,event):
        print("Close")
        self.Destroy()

     def onClickYesButton(self,event):


        filePath = "../wcmEthRecData/activityTrack/"
        file_exists = exists(filePath)

        if(file_exists == False):
            print("File does not exist!")
            os.mkdir(filePath)
            header = ['Time:', 'Value']

            data = [[getDateTime(), "Activity registered!"]]

            filePathName = filePath + "activity.csv"

            writeToCSV(filePathName,header,data)
            
        else:
            header = ['Time:', 'Value']

            data = [[getDateTime(), "Activity registered!"]]

            filePathName = filePath + "activity.csv"

            appendToCSV(filePathName,header,data)





        print("Yes was clicked.")
        a = nasaTLXWindow(self,"").Show()
        #https://stackoverflow.com/questions/34297265/wxpython-automatically-closing-nested-modal-dialogs
        lst = wx.GetTopLevelWindows()
        lst[1].Hide()
        #print(lst)
        # for i in range(len(lst) - 1, 0, -1):
        #     if isinstance(lst[i], wx.Dialog):
        #         print "Closing " + str(lst[i])
        #         lst[i].Close(True)




     def onClickNoButton(self,event):
        print("No was clicked.")

        filePath = "../wcmEthRecData/activityTrack/"
        file_exists = exists(filePath)

        if(file_exists == False):
            print("File does not exist!")
            os.mkdir(filePath)
            header = ['Time:', 'Value']

            data = [[getDateTime(), "Activity registered!"]]

            filePathName = filePath + "activity.csv"

            writeToCSV(filePathName,header,data)
            
        else:
            header = ['Time:', 'Value']

            data = [[getDateTime(), "Activity registered!"]]

            filePathName = filePath + "activity.csv"

            appendToCSV(filePathName,header,data)


        self.closeFunc(event)


'''
/////////////////////////////////////////////////////////////////
////// testFrame (WIP) Needs a better name.            //////////////////////
Note: "testFrame" is the first window that is opened upon starting the python
application. This window acts as a junction for the different modal windows
associated with the application. Of note, when the participant presses 
"onSwitchButtonClick", depending if the boolean value recordStatus is True,
the application will run a threaded process that will record user screen activity 
for a period of 5 minutes. Currently, the video is saved to a hard coded to
a specific directory.
/////////////////////////////////////////////////////////////////
''' 
class testFrame(experienceSampleNASATLX.wcmEthnographyApp):
    recordStatus = True
    recordToggle = False


    def __init__(self,parent):
        experienceSampleNASATLX.wcmEthnographyApp.__init__(self,parent)  
        
    def onSwitchButtonClick(self,event):
        a = surveyRequestDialog(self,"").Show()

        print("On switch button is clicked!")

        # print(self.recordStatus)
        if( (self.recordToggle == True) and (self.recordStatus == True) ):
            self.recordStatus = False
            print("Screen record thread initating.")
            screenRecThread = threading.Thread(target=self.screenRecord)
            screenRecThread.start()
        else:
            print("No recording will take place.")
    
    def eodSurveyClick(self,event):
        print("EOD survey button is clicked!")
        a = eodSurvey(self,"").Show()


    def onRecordCheck(self,event):

        recordCheckVal = event.GetEventObject().GetValue()
        if(recordCheckVal == True):
            self.recordToggle = recordCheckVal
            print("Record button was checked! Record status value: " + str(self.recordToggle))
        else:
            self.recordToggle = recordCheckVal
            print("Record button was unchecked! Record status value: " + str(self.recordToggle))

        # cb = e.GetEventObject() 
        #   print(cb.GetLabel(),' is clicked',cb.GetValue())
        #   testRecVal = cb.GetValue()
        #   if(testRecVal ==  True):
        #         self.recordStatus = testRecVal
        #         print(self.recordStatus)

    def onGoToRecordData(self,event):
        print("Go to record data button was clicked!")
        #https://stackoverflow.com/questions/71083145/how-to-open-a-finder-at-the-current-dir-on-mac-os-in-python
        open_file("../wcmEthRecData")



    def onMenuQuit(self,event):
        self.Destroy()

    def screenRecord(self):
        # Define vars:
        # Specify resolution
        SCREEN_SIZE = pyautogui.size()

        # Specify video codec
        codec = cv2.VideoWriter_fourcc(*"avc1")
         
        # Specify name of Output file
        filename = "Recording.mp4"
        
        # Specify frames rate. We can choose any
        # value and experiment with it
        fps = 1.0
            
        # Creating a VideoWriter object
        out = cv2.VideoWriter(filename, codec, fps, (1440,900))
     
        # Create window objects:
        # Create an Empty window
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
         
        # Resize this window
        cv2.resizeWindow("Live", 1440,900)

        for x in range(0, 50):
            #while True:
            # Take screenshot using PyAutoGUI
            #img = pyautogui.screenshot()
         
            # Convert the screenshot to a numpy array
            # frame = np.array(img)
            frame =  np.array(ImageGrab.grab(bbox=(0,0,1440,900)))
         
            # Convert it from BGR(Blue, Green, Red) to
            # RGB(Red, Green, Blue)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
         
            # Write it to the output file
            out.write(frame)
             
            # Optional: Display the recording screen
            cv2.imshow('Live', frame)
            print(x)
             
            # Stop recording when we press 'q'
            # if cv2.waitKey(1) == ord('q'):
            #     break
         
        # Release the Video writer
        out.release()
         
        # Destroy all windows
        cv2.destroyAllWindows()
        print("Video recording complete!")
        self.recordStatus = True

'''
/////////////////////////////////////////////////////////////////
////// Setting up main program loop /////////////////////////////
/////////////////////////////////////////////////////////////////
'''


# Refer to this link to understand basic structure of wxPython GUI
# programming:
# https://www.tutorialspoint.com/wxpython/wxpython_hello_world.htm
        
app = wx.App(False) #Defines an object of Applicaiton class
frame = testFrame(None) # Creates top level window as object of wx.Frame class.
						# See "testFrame" class above
frame.Show(True) 	#Activate frame window by  "show()" method
#start the applications 
app.MainLoop() #Enter main event loop of Application object