import vtk
import math
import wx
# create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
 
# create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
i=0
sourc=[]
mapper=[]
actor=[]
for i in range(0,360):
    sourc.append(vtk.vtkCylinderSource())
    sourc[i].SetRadius(0.3)
    sourc[i].SetHeight(7)

    sourc[i].SetCenter(2*math.cos(i),0,2*math.sin(i))
    sourc[i].SetResolution(100.0)
    sourc[i].Update() 

    mapper.append(vtk.vtkPolyDataMapper())
    mapper[i].SetInput(sourc[i].GetOutput())

    actor.append(vtk.vtkActor())
    actor[i].SetMapper(mapper[i])
    actor[i].SetOrigin(0,0,0)
    actor[i].RotateX(90)
    actor[i].GetProperty().SetOpacity(1)

    #actor[i].SetPosition(2*cos(i),2*sin(i),0)
    ren.AddActor(actor[i])

    i=i+1
# create source
#
transform = vtk.vtkTransform()
transform.Translate(0.0, 0.0, 3.5)
 
axes = vtk.vtkAxesActor()
#  The axes are positioned with a user transform
axes.SetUserTransform(transform)
 
# properties of the axes labels can be set as follows
# this sets the x axis label to red
# axes->GetXAxisCaptionActor2D()->GetCaptionTextProperty()->SetColor(1,0,0);
 
# the actual text of the axis label can be changed:
# axes->SetXAxisLabelText("test");
 
ren.AddActor(axes)


source = vtk.vtkDiskSource()
source.SetInnerRadius(1.6)
source.SetOuterRadius(3)
source.SetRadialResolution(100)
source.SetCircumferentialResolution(100)
source.Update()
 
# mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInput(source.GetOutput())
 
# actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetOrigin(0,0,0)
# assign actor to the renderer
ren.AddActor(actor)
response = raw_input("Please enter your name: ")
print response
actor.SetPosition(0.0,0.0,float(response))
actor.GetProperty().SetColor(0.5,0.0,0.0)
# enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()

