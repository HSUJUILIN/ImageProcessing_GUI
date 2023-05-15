# ImageProcessing_GUI
Image processing by GUI Tkinter)
This repositories is still being organized!!!

1. cv2_ThresholdByTrackBar.py

    Introduction:    
        Apply GUI to output the threshold number

    Version:  
        first release: (GMT+8) 2020/10/17 17:30 finish.  
        second release: (GMT+8) 2022/08/08 14:37 simplify the code.

    Note:  
        
    State:  
        Finish

2. cv2_SelectROI.py

    Introduction:  
        Apply GUI to output the coordinate of the ROI

    Version:  
        first release: (GMT+8) 2020/11/07 16:48 finish.  
        second release: (GMT+8) 2021/04/20 14:37 simplify the code.

    Note:  

    State:  
        Unfinish  

3. GUIPanel.py

    Introduction:  
        Integrate the method of the image process

    Version:  
        first edit: (GMT+8) 2022/08/11 Create the panel and design the user interface.  
        second edit: (GMT+8) 2023/04/11 17:15 Add preview image function.  
        third edit: (GMT+8) 2023/04/13 17:28 Add image imformation and the real-time state window (scrollbar).
        fourth edit: (GMT+8) 2023/04/17 15:38 Add ticks, "Quit" event(tick), and the pop-up messagebox before closed GUI.
        fifth edit: (GMT+8) 2023/04/19 17:31 Add the display of "Right Panel".
        sixth edit: (GMT+8) 2023/04/25 16:31 Tune the left-bottom frame.
        seventh edit: (GMT+8) 2023/05/01 21:13 Tune the image information, add the bottom and the entry. 
        eighth edit: (GMT+8) 2023/05/05 18:00 Add the scale widget and the checkbox of threshold function.

    Note:  
        Threshold, Gaussian Blur(custom kernel size). RealTime threshold value.
        
    Process:
        If the checkbox is START("1"), we can get the value of scale widget. If the checkbox is END("0"), we can't get.
