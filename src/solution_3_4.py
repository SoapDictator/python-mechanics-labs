import sympy as sym
import matplotlib.style as mplstl
import sympy.plotting as symplot

mplstl.use('seaborn-whitegrid')

t = sym.Symbol('t')
om = sym.Symbol('om')

A = 0.01
k = 0.4
m0 = 0.1

# 4
delta = []
r_val = [0.05, 0.07, 0.10]
om_val = [1, 2, 3]
A = []
fi = []
x3 = []

for i in range(0, len(r_val)):
	delta.append(r_val[i] / (2 * m0))
delta0 = delta[0]

for i in range(0, len(om_val)):
	A.append(1 / (sym.sqrt((omega0**2 - om_val[i]**2)**2 + 4 * delta0**2 * om_val[i]**2)))
	fi.append(sym.atan(2 * delta0 * om_val[i] / (omega0**2 - om_val[i]**2)))
	
	x3.append(A[i] * sym.cos(t * om_val[i] + fi[i]))
	
x3_1_plot = sym.plot(
	x3[0], (t, 0, 6),
	label='om=1',
	line_color='b',
	legend=True,
	show=False)

x3_2_plot = sym.plot(
	x3[1], (t, 0, 6),
	label='om=2',
	line_color='r',
	legend=True,
	show=False)
x3_1_plot.extend(x3_2_plot)

x3_3_plot = sym.plot(
	x3[2], (t, 0, 6),
	label='om=3',
	line_color='g',
	legend=True,
	show=False)
x3_1_plot.extend(x3_3_plot)
	
x3_1_plot.title = 'Зависимость координаты материальной точки x от времени t'
x3_1_plot.xlabel = 't, с'
x3_1_plot.ylabel = 'x, м'
x3_1_plot.show()

A_expr = 1 / (sym.sqrt((omega0**2 - om**2)**2 + 4 * delta0**2 * om**2))
fi_expr = sym.atan(2 * delta0 * om / (omega0**2 - om**2))
x3_expr = A_expr * sym.cos(t * om + fi_expr)

x3_plot3d = symplot.plot3d(
    x3_expr, (t, 0, 6), (om, om_val[0], om_val[len(om_val)-1]),
	show=False)
x3_plot3d.title = ('Зависимость коорд. мат. точки x '
    'от времени t и вынуждающей силы omega')
x3_plot3d.xlabel = 't, с'
x3_plot3d.ylabel = 'omega'
x3_plot3d.show()