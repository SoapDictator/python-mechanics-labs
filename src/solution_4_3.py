import sympy as sym
import matplotlib.style as mplstl
import sympy.plotting as symplot

mplstl.use('seaborn-whitegrid')

t = sym.Symbol('t')

a1 = 0.2
a2 = 0.3
om1 = 2
om2 = 1

fi1 = sym.pi/4
fi2 = sym.pi/3

# 3
x1 = a1 * sym.sin(om1 * t + fi1)
x2 = a2 * sym.sin(om2 * t + fi2)
	
x_plot = sym.plot_parametric(
	x1, x2, (t, 0, 7),
	show = False)
	
x_plot.title = 'Фигура Лиссажу'
x_plot.show()