#!/usr/bin/python

import xml.etree.ElementTree as ET, glob, sys, os

files = glob.glob("*.xml")
TotalSueldos = 0
TotalExento = 0
TotalGravado = 0
TotalImpuestosRetenidos = 0
Deducciones = 0
SueldoDeclaracion = 0
LimiteInferior = 0
CuotaFija = 0
Excedente = 0
ImpuestosPagarSubtotal = 0
ImpuestosPagarTotal = 0
Tasa = 0
SaldoFinal = 0
for file in files:
	tree = ET.parse(file)
	root = tree.getroot()

	renglon  = ''

	stamp = root.find('.//*[@TotalGravado]')
	if stamp is not None:
		TotalGravado = TotalGravado + float(stamp.attrib.get('TotalGravado'))

	if stamp is not None:
		TotalSueldos = TotalSueldos + float(stamp.attrib.get('TotalSueldos'))

	if stamp is not None:
		TotalExento = TotalExento + float(stamp.attrib.get('TotalExento'))
	
	stamp = root.find('.//*[@TotalImpuestosRetenidos]')
	if stamp is not None:
		TotalImpuestosRetenidos = TotalImpuestosRetenidos + float(stamp.attrib.get('TotalImpuestosRetenidos'))


	
Deducciones = float(input('Ingrese Deducciones:'))
SueldoDeclaracion = TotalGravado - Deducciones

if SueldoDeclaracion < float(103550.44):
	LimiteInferior = float(58922.17)
	CuotaFija = float(3460.01)
	Tasa = float(10.88) / 100
elif SueldoDeclaracion < float(120372.83):
	LimiteInferior = float(103550.45)
	CuotaFija = float(8315.57)
	Tasa = float(16.00) / 100
elif SueldoDeclaracion < float(144119.23):
	LimiteInferior = float(120372.84)
	CuotaFija = float(11007.14)
	Tasa = float(17.92) / 100
elif SueldoDeclaracion < float(290667.75):
    LimiteInferior = float(144119.24)
    CuotaFija = float(15262.49)
    Tasa = float(21.36) / 100
elif SueldoDeclaracion < float(458132.29):
	LimiteInferior = float(290667.76)
	CuotaFija = float(46565.26)
	Tasa = float(23.52) / 100		

Excedente = SueldoDeclaracion - LimiteInferior
ImpuestosPagarSubtotal = Excedente * Tasa
ImpuestosPagarTotal = ImpuestosPagarSubtotal + CuotaFija
SaldoFinal = TotalImpuestosRetenidos - ImpuestosPagarTotal

print " + Total Sueldo:" + str(TotalSueldos)
print " - Total Exento:" + str(TotalExento)
print "-------------------------------"
print " = Total Gravado:" + str(TotalGravado)
print " - Deducciones:" + str(Deducciones)
print "-------------------------------"
print "Ingreso Anual para la declaracion:" + str(SueldoDeclaracion)
print "Limite inferior:" + str(LimiteInferior)
print "   Excedente:" + str(Excedente)
print "   ImpuestosPagarSubtotal:" + str(ImpuestosPagarSubtotal)
print " + Couta fija:" + str(CuotaFija)
print "-------------------------------"
print " Impuestos A pagar:" + str(ImpuestosPagarTotal)
print " Impuestos Retenidos:" + str(TotalImpuestosRetenidos)
print "---------------RESULTADO--------------------"
print " Saldo Final:" + str(SaldoFinal)