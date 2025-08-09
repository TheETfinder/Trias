import xmlschema
import pprintpp
xsd = xmlschema.XMLSchema('Trias_StopEvents.xsd')
xml = xsd.to_dict('kvv.xml')


