import sympy as sym
import matplotlib.style as mplstl
import sympy.plotting as symplot

mplstl.use('seaborn-whitegrid')

t = sym.Symbol('t')

a1 = 1
om1 = 48
om2 = 52

# 2
x1 = a1 * sym.sin(om1 * t)
x2 = a1 * sym.sin(om2 * t)
xr = x1 + x2

xo = 2 * a1 * sym.cos((om2 - om1) * t / 2)
	
x_1_plot = sym.plot(
	xr, (t, 0, 6),
	label='x1+x2',
	line_color='b',
	legend=True,
	show=False)

x_2_plot = sym.plot(
	xo, (t, 0, 6),
	label='огибающая',
	line_color='r',
	legend=True,
	show=False)
x_1_plot.extend(x_2_plot)
	
x_1_plot.title = 'Зависимость смещения маятника от времени'
x_1_plot.xlabel = 't, с'
x_1_plot.ylabel = 'x, м'
x_1_plot.show()