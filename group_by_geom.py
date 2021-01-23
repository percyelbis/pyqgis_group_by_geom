'''
Este Script agrupa por tipo geometria (Puntos, Lineas, Poligonos).
Autor: Percy Elbis
'''
puntos = 'qgis_puntos'
lineas = 'qgis_lineas'
poligonos = 'qgis_poligonos'
group = root.addGroup(puntos)
group1 = root.addGroup(lineas)
group2 = root.addGroup(poligonos)
root = QgsProject.instance().layerTreeRoot()
self=qgis.utils
vlayer = self.iface.mapCanvas().layers()
for i in vlayer:
    if i.type() == QgsMapLayer.VectorLayer:
        if i.geometryType() == 0:
            name = i.id()
            layer = root.findLayer(name)
            clone = layer.clone()
            group.insertChildNode(0, clone)
            root.removeChildNode(layer)
        elif i.geometryType() == 1:
            name = i.id()
            layer = root.findLayer(name)
            clone = layer.clone()
            group1.insertChildNode(0, clone)
            root.removeChildNode(layer)
        elif i.geometryType() == 2:
            name = i.id()
            layer = root.findLayer(name)
            clone = layer.clone()
            group2.insertChildNode(0, clone)
            root.removeChildNode(layer)

iface.messageBar().pushMessage("qgis", "Agrupo correctamente!!!", level=Qgis.Info, duration=1)


        

