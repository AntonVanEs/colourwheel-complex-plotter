import pygame
import colorsys
import cmath
import tkFileDialog
import time

zoomFactor=1.5

tau=2*cmath.pi
e=cmath.e
i=cmath.sqrt(-1)

def colourWheel(z):
    a=z.real
    b=z.imag
    
    r=abs(z)
    p=cmath.phase(z)
    
    if p<0:
        p=tau+p
    
    H=p/tau
    L=1-(cmath.exp(-cmath.log(r+1))).real
    return [255*n for n in colorsys.hls_to_rgb (H,L,1)]

def plot(formula, Xmin, Xmax, Ymin, Ymax, resolution):
    if Xmax<=Xmin:
        raise ValueError('Xmax must be larger than Xmin')
    if Ymax<=Ymin:
        raise ValueError('Ymax must be larger than Ymin')

    width = Xmax-Xmin
    height= Ymax-Ymin

    screenWidth = int(width*resolution)
    screenHeight= int(height*resolution)
    
    if not pygame.display.get_init:
        pygame.display.init
    
    screen=pygame.display.set_mode([screenWidth,screenHeight])
    pygame.display.set_caption('complex plotter: '+formula)
    try:
        for Y in range(screenHeight):
            b=Ymax-(float(Y)/resolution)
            for X in range(screenWidth):
                a=Xmin+(float(X)/resolution)

                z=a+b*i
        
                try:
                    exec("y="+formula)
                    c=colourWheel(y)
                    screen.set_at((X, Y), c)
                except:
                    c=[255,255,255]
                    screen.set_at((X, Y), c)
                
            pygame.display.flip()
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        print("saving file, please give a path...")
                        path=str(tkFileDialog.asksaveasfile(defaultextension=".png"))[13:-26]
                        surface=pygame.display.get_surface()
                        pygame.image.save(surface,path)
                        print("saved as: "+path)
                        
                    if event.key == pygame.K_ESCAPE:
                        raise KeyboardInterrupt()

                    if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                        (X,Y)=pygame.mouse.get_pos()

                        newXmin=(Xmin+(float(X)/resolution))-( width/(2*zoomFactor))
                        newXmax=(Xmin+(float(X)/resolution))+( width/(2*zoomFactor))
                        newYmin=(Ymax-(float(Y)/resolution))-(height/(2*zoomFactor))
                        newYmax=(Ymax-(float(Y)/resolution))+(height/(2*zoomFactor))

                        newResolution=resolution*zoomFactor

                        print("plot(\""+formula+"\","+str(newXmin)+","+str(newXmax)+","+str(newYmin)+","+str(newYmax)+","+str(newResolution)+")")
                        exec(("plot(\""+formula+"\","+str(newXmin)+","+str(newXmax)+","+str(newYmin)+","+str(newYmax)+","+str(newResolution)+")"))
                        return ""

                    if event.key == pygame.K_MINUS:
                        (X,Y)=pygame.mouse.get_pos()

                        newXmin=(Xmin+(float(X)/resolution))-( width*zoomFactor/2)
                        newXmax=(Xmin+(float(X)/resolution))+( width*zoomFactor/2)
                        newYmin=(Ymax-(float(Y)/resolution))-(height*zoomFactor/2)
                        newYmax=(Ymax-(float(Y)/resolution))+(height*zoomFactor/2)

                        newResolution=resolution/zoomFactor

                        print("plot(\""+formula+"\","+str(newXmin)+","+str(newXmax)+","+str(newYmin)+","+str(newYmax)+","+str(newResolution)+")")
                        exec(("plot(\""+formula+"\","+str(newXmin)+","+str(newXmax)+","+str(newYmin)+","+str(newYmax)+","+str(newResolution)+")"))
                        return ""

                    if event.key == pygame.K_PAGEUP:
                        newResolution=resolution*zoomFactor

                        print("plot(\""+formula+"\","+str(Xmin)+","+str(Xmax)+","+str(Ymin)+","+str(Ymax)+","+str(newResolution)+")")
                        exec(("plot(\""+formula+"\","+str(Xmin)+","+str(Xmax)+","+str(Ymin)+","+str(Ymax)+","+str(newResolution)+")"))
                        return ""

                    if event.key == pygame.K_PAGEDOWN:
                        newResolution=resolution/zoomFactor

                        print("plot(\""+formula+"\","+str(Xmin)+","+str(Xmax)+","+str(Ymin)+","+str(Ymax)+","+str(newResolution)+")")
                        exec(("plot(\""+formula+"\","+str(Xmin)+","+str(Xmax)+","+str(Ymin)+","+str(Ymax)+","+str(newResolution)+")"))
                        return ""
    
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        print("saving file, please give a path...")
                        path=str(tkFileDialog.asksaveasfile(defaultextension=".png"))[13:-26]
                        surface=pygame.display.get_surface()
                        pygame.image.save(surface,path)
                        print("saved as: "+path)
                        
                    if event.key == pygame.K_ESCAPE:
                        raise KeyboardInterrupt()

                    if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                        (X,Y)=pygame.mouse.get_pos()

                        newXmin=(Xmin+(float(X)/resolution))-( width/(2*zoomFactor))
                        newXmax=(Xmin+(float(X)/resolution))+( width/(2*zoomFactor))
                        newYmin=(Ymax-(float(Y)/resolution))-(height/(2*zoomFactor))
                        newYmax=(Ymax-(float(Y)/resolution))+(height/(2*zoomFactor))

                        newResolution=resolution*zoomFactor

                        print("plot(\""+formula+"\","+str(newXmin)+","+str(newXmax)+","+str(newYmin)+","+str(newYmax)+","+str(newResolution)+")")
                        exec(("plot(\""+formula+"\","+str(newXmin)+","+str(newXmax)+","+str(newYmin)+","+str(newYmax)+","+str(newResolution)+")"))
                        return ""

                    if event.key == pygame.K_MINUS:
                        (X,Y)=pygame.mouse.get_pos()

                        newXmin=(Xmin+(float(X)/resolution))-( width*zoomFactor/2)
                        newXmax=(Xmin+(float(X)/resolution))+( width*zoomFactor/2)
                        newYmin=(Ymax-(float(Y)/resolution))-(height*zoomFactor/2)
                        newYmax=(Ymax-(float(Y)/resolution))+(height*zoomFactor/2)

                        newResolution=resolution/zoomFactor

                        print("plot(\""+formula+"\","+str(newXmin)+","+str(newXmax)+","+str(newYmin)+","+str(newYmax)+","+str(newResolution)+")")
                        exec(("plot(\""+formula+"\","+str(newXmin)+","+str(newXmax)+","+str(newYmin)+","+str(newYmax)+","+str(newResolution)+")"))
                        return ""

                    if event.key == pygame.K_PAGEUP:
                        newResolution=resolution*zoomFactor

                        print("plot(\""+formula+"\","+str(Xmin)+","+str(Xmax)+","+str(Ymin)+","+str(Ymax)+","+str(newResolution)+")")
                        exec(("plot(\""+formula+"\","+str(Xmin)+","+str(Xmax)+","+str(Ymin)+","+str(Ymax)+","+str(newResolution)+")"))
                        return ""

                    if event.key == pygame.K_PAGEDOWN:
                        newResolution=resolution/zoomFactor

                        print("plot(\""+formula+"\","+str(Xmin)+","+str(Xmax)+","+str(Ymin)+","+str(Ymax)+","+str(newResolution)+")")
                        exec(("plot(\""+formula+"\","+str(Xmin)+","+str(Xmax)+","+str(Ymin)+","+str(Ymax)+","+str(newResolution)+")"))
                        return ""
                    
                if pygame.mouse.get_pressed()[0]:
                    (X,Y)=pygame.mouse.get_pos()
                    
                    a=Xmin+(float(X)/resolution)
                    b=Ymax-(float(Y)/resolution)

                    if a>=0: print "",
                    if b>=0:
                       print str(a)+"+"+str(b)+"i",
                    else:
                        print str(a)+str(b)+"i",

                    print "->",
                    
                    z=a+b*i
                    try:
                        exec("y="+formula)
                        a=y.real
                        b=y.imag
                    

                        if a>=0: print "",
                        if b>=0:
                           print str(a)+"+"+str(b)+"i"
                        else:
                            print str(a)+str(b)+"i"
                    except:
                        print "error"
                    
                    while pygame.mouse.get_pressed()[0]:
                        pygame.display.update()
                        pygame.event.get()
                        
    except KeyboardInterrupt:
        pygame.display.quit()

    
