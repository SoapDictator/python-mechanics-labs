import sympy as sym
import matplotlib.style as mplstl
import sympy.plotting as symplot

mplstl.use('seaborn-whitegrid')
line_colors = ['b', 'r', 'g', 'y', 't']

t = sym.Symbol('t')
r = sym.Symbol('r')

A = 0.01
k = 0.4
m0 = 0.1

# 3
r_val = [0.05, 0.07, 0.10]
delta = []
x2 = []

for i in range(0, len(r_val)):
	delta.append(r_val[i] / (2 * m0))
	
for i in range(0, len(delta)):
	x2.append(A * sym.cos(t * omega0) * sym.exp(-t * delta[i]))
	
x2_plot = sym.plot(legend=True, show=False)

for j in range(0, len(delta)):
	label = 'r='+str(r_val[j])
	
	x2_ext_plot = sym.plot(
		x2[j], (t, 0, 6),
		label=label,
		line_color=line_colors[j],
		legend=True,
		show=False)
	x2_plot.extend(x2_ext_plot)
	
x2_plot.title = 'Зависимость координаты материальной точки x от времени t'
x2_plot.xlabel = 't, с'
x2_plot.ylabel = 'x, м'
x2_plot.show()

x2_expr = A * sym.cos(t * omega0) * sym.exp(-t * (r / (2 * m0)))

x2_plot3d = symplot.plot3d(
    x2_expr, (t, 0, 6), (r, r_val[0], r_val[len(r_val)-1]),
	show=False)

x2_plot3d.title = ('Зависимость коорд. мат. точки x '
    'от времени t и коэфф. вязкого трения r')
x2_plot3d.xlabel = 't, с'
x2_plot3d.ylabel = 'r'
x2_plot3d.show()