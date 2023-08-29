class TV:
	numTV = 0
	
	def __init__(self, marca, estado):
		self._marca = marca
		self._estado = estado
		self._control = None
		self._canal = 1
		self._precio = 500
		self._volumen = 1
		
		TV.numTV += 1

	def canalUp(self):
		self.setCanal(self._canal + 1)

	def canalDown(self):
		self.setCanal(self._canal - 1)

	def volumenUp(self):
		self.setVolumen(self._volumen + 1)

	def volumenDown(self):
		self.setVolumen(self._volumen - 1)

	def getEstado(self):
		return self._estado

	def turnOn(self):
		self._estado = True

	def turnOff(self):
		self._estado = False

	def getMarca(self):
		return self._marca

	def getCanal(self):
		return self._canal
	
	def getPrecio(self):
		return self._precio

	def getVolumen(self):
		return self._volumen

	def getControl(self):
		return self._control

	def setMarca(self, marca):
		if (self._estado and self._marca >= 1 and self._marca <= 120):
			self._marca = marca

	def setCanal(self, canal):
		self._canal = canal
	
	def setPrecio(self, precio):
		self._precio = precio

	def setVolumen(self, volumen):
		if (self._estado and self._volumen >= 0 and self._volumen <= 7):
			self._volumen = volumen

	def setControl(self, control):
		self._control = control