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
quad=[]
quads=[]
polydata=[]
for i in range(0,360):
   


 
    # Create four points (must be in counter clockwise order)
    p0 = [0.0, 0.0, 0.0]
    p1 = [4.0, 0.0, 0.0]
    p2 = [4.0, 10.0, 0.0]
    p3 = [0.0, 10.0, 0.0]
     
    # Add the points to a vtkPoints object
    points = vtk.vtkPoints()
    points.InsertNextPoint(p0)
    points.InsertNextPoint(p1)
    points.InsertNextPoint(p2)
    points.InsertNextPoint(p3)
     
    # Create a quad on the four points
    quad.append(vtk.vtkQuad())
    quad[i].GetPointIds().SetId(0,0)
    quad[i].GetPointIds().SetId(1,1)
    quad[i].GetPointIds().SetId(2,2)
    quad[i].GetPointIds().SetId(3,3)
     
    # Create a cell array to store the quad in
    quads.append(vtk.vtkCellArray())
    quads[i].InsertNextCell(quad[i])
     

    # Create a polydata to store everything in
    polydata.append(vtk.vtkPolyData())
     
    # Add the points and quads to the dataset
    polydata[i].SetPoints(points)
    polydata[i].SetPolys(quads[i])

    mapper.append(vtk.vtkPolyDataMapper())
    mapper[i].SetInput(polydata[i])

    actor.append(vtk.vtkActor())
    actor[i].SetMapper(mapper[i])
    actor[i].SetOrigin(0,0,4)
    actor[i].RotateY(i)
    #actor[i].SetPosition(2*math.cos(i),0,2*math.sin(i))
    actor[i].GetProperty().SetOpacity(1)
    actor[i].GetProperty().SetColor(0.2,0.2,0.5)

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

