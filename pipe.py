import vtk
 
# create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
 
# create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
i=1
sourc=[]
mapper=[]
actor=[]
for i in range(0,100):
    sourc.append(vtk.vtkDiskSource())
    sourc[i].SetInnerRadius(1.5)
    sourc[i].SetOuterRadius(2)
    sourc[i].SetRadialResolution(100)
    sourc[i].SetCircumferentialResolution(100)
    sourc[i].Update() 

    mapper.append(vtk.vtkPolyDataMapper())
    mapper[i].SetInput(sourc[i].GetOutput())

    actor.append(vtk.vtkActor())
    actor[i].SetMapper(mapper[i])
    actor[i].SetPosition(0,0,i/10)
    ren.AddActor(actor[i])

    i=i+1
# create source
source = vtk.vtkDiskSource()

source.SetInnerRadius(1.5)
source.SetOuterRadius(2)
source.SetRadialResolution(100)
source.SetCircumferentialResolution(100)
source.Update()
 
source1 = vtk.vtkDiskSource()
source1.SetInnerRadius(1.5)
source1.SetOuterRadius(2)
source1.SetRadialResolution(100)
source1.SetCircumferentialResolution(100)
source1.Update()
# mapper
mapper0 = vtk.vtkPolyDataMapper()
mapper0.SetInput(source.GetOutput())
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInput(source1.GetOutput())

# actor
actor0 = vtk.vtkActor()
actor0.SetMapper(mapper0)
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor0.SetPosition(0,0,1)
actor1.SetPosition(0,0,-1)
# assign actor to the renderer
ren.AddActor(actor0)
ren.AddActor(actor1)
 
# enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()