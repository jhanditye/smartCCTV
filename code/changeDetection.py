def keepLargeComponents(I,th):
    '''
    Purpose: Keeps large connected components together
    '''
    R = np.zeros(I.shape)<0
    unique_labels = np.unique(I.flatten())
    # not that background labelled zero
    for label in unique_labels:
        if label == 0:
            pass
        else: 
            I2 = I==label
            if np.sum(I2)>th:
                R  = R | I2
    return np.float32(255*R)



def alphaBlend(foreground, background, alpha):
    '''
    Purpose: Layers one photo 'alpha' onto 'background' with 'alpha' getting its colours from 'foreground'
    '''

    foregroundNew = foreground.astype(float)
    backgroundNew = background.astype(float)
    alphaNew = alpha.astype(float)/255

    foregroundNew = cv2.multiply(alphaNew,foregroundNew)
    backgroundNew = cv2.multiply(1.0-alphaNew, backgroundNew)

    outImage = cv2.add(foregroundNew,backgroundNew)
    
    return outImage/255

## Useful Helper Functions

def saveSeq(framesArray,counter,threshold,outputPath):
    '''
    Purpose: Puts bounding boxes around images in a given array and saves them to an appropriate path
    '''
    if len(framesArray)< threshold:
        pass
    else:
        counter = 1
        for frame in framesArray:

            # Find somewhere to store the image
            imgName = f"image_{counter}.jpg"
            finalPath = os.path.join(outputPath,imgName)

            # draw bounding boxes
            bbox, labels, conf = cv.detect_common_objects(frame)
            frame = draw_bbox(frame,bbox,labels,conf)

            cv2.imwrite(finalPath,frame)
            counter +=1
            
def displaySeq(outputPath):
    '''
    Purpose: Display a sequence of saved images 
    '''
    for imgName in os.listdir(outputPath):
        frame = cv2.imread(os.path.join(outputPath,imgName))
        frame = cv2.resize(frame,dsize = (1200,800))
        cv2.imshow('Displayy',frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break       
    cv2.destroyAllWindows()


def smartCCTV(vidPath, outputPath,counterThreshold = 100):


    '''
    Purpose: Given a video, the function will cleanly find changes to the background.
    It will use this information to detect and track relevant changes. 
    
    To do: If the detected behaviour is suspicious, label the data appropriately and send away the video snippet 
    evidence
    '''

    cap = cv2.VideoCapture(vidPath)
    fgModel = cv2.createBackgroundSubtractorMOG2()

    ## Initialise some values
    indexArray = []
    framesArray = []
    counter = 0
    framesThreshold = 5
    while(1):
        counter += 1
        
        ret, frame = cap.read() # gives us the individual frames
        frame = cv2.resize(frame,dsize = (1200,800))
        fgmask = fgModel.apply(frame)
        
        ## Denoising using morphology - dilation and erosion
        kernel  = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
        fgmask = cv2.morphologyEx(np.float32(fgmask),cv2.MORPH_OPEN,kernel)
        
        # Improve denoising by considering connected components
        _, labels_img = cv2.connectedComponents(np.array(fgmask>0,np.uint8))
        fgmask = keepLargeComponents(labels_img,400)

        alpha = np.zeros(frame.shape,np.uint8)
        alpha[:,:,0],alpha[:,:,1],alpha[:,:,2] = fgmask,fgmask,fgmask
        background = np.zeros(frame.shape,np.uint8)

        colouredBackground = alphaBlend(frame, background,alpha)
        # Detect change in foreground and save it 
        if np.sum(fgmask)>0:
            indexArray.append(counter)
            framesArray.append(frame)
        if len(indexArray) >=2 and indexArray[-1]> indexArray[-2]+1:
            saveSeq(framesArray,counter,framesThreshold,outputPath)
        
        # Look at changes side by side with frame
        sideBySide  = np.hstack((frame/255,colouredBackground))
        
        cv2.imshow('Display Window', sideBySide)
        k = cv2.waitKey(20) & 0xff 

        if counter  == counterThreshold:
            break
    saveSeq(framesArray,counter,framesThreshold,outputPath)
    cap.release()
    cv2.destroyAllWindows()    