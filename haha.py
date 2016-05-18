import sys
from PyQt4 import QtGui
import numpy as np
from matplotlib.figure import Figure
# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class MyChart(FigureCanvas):
	def __init__(self):
		# Standard Matplotlib code to generate the plot
		self.fig = Figure()
		self.axes = self.fig.add_subplot(111)
		
		size = 50*np.random.randn(1000)
		colors = np.random.rand(1000)
		x = np.random.randn(1000)
		y = np.random.randn(1000)
		self.axes.scatter(x, y, s=size, c=colors)
		self.axes.set_title('Hello, World!')

		# initialize the canvas where the Figure renders into
		FigureCanvas.__init__(self, self.fig)

qApp = QtGui.QApplication(sys.argv)

mc = MyChart()
mc.show()

sys.exit(qApp.exec_())