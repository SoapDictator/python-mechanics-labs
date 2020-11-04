import sympy as sym
import matplotlib.style as mplstl
import sympy.plotting as symplot

mplstl.use('seaborn-whitegrid')

t = sym.Symbol('t')

a1 = 0.2
a2 = 0.3
om1 = 2

fi1 = sym.pi/4
fi2 = sym.pi/3

# 1
x1 = a1 * sym.sin(om1 * t + fi1)
x2 = a2 * sym.sin(om1 * t + fi2)
xr = x1 + x2
	
x_1_plot = sym.plot(
	x1, (t, 0, 6),
	label='x1',
	line_color='b',
	legend=True,
	show=False)

x_2_plot = sym.plot(
	x2, (t, 0, 6),
	label='x2',
	line_color='r',
	legend=True,
	show=False)
x_1_plot.extend(x_2_plot)

x_3_plot = sym.plot(
	xr, (t, 0, 6),
	label='x1+x2',
	line_color='g',
	legend=True,
	show=False)
x_1_plot.extend(x_3_plot)
	
x_1_plot.title = 'Зависимость смещения маятника от времени'
x_1_plot.xlabel = 't, с'
x_1_plot.ylabel = 'x, м'
x_1_plot.show()