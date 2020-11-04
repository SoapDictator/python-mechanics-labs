import sympy as sym
import matplotlib.style as mplstl
import sympy.plotting as symplot

mplstl.use('seaborn-whitegrid')
line_colors = ['b', 'r', 'g', 'y', 't']

t = sym.Symbol('t')
m = sym.Symbol('m')

A = 0.01
k = 0.4
m0 = 0.1

# 2
m_count = 3
x1 = []

omega = sym.sqrt(k / m)
omega_func = sym.lambdify(m, omega)

for i in range(0, m_count):
	x1.append(sym.cos(t * omega_func((i+1) * m0)))

x1_plot = sym.plot(legend=True, show=False)

for j in range(0, m_count):
	label = str(j+1)+'*m0'
	
	x1_ext_plot = sym.plot(
		x1[j], (t, 0, 6),
		label=label,
		line_color=line_colors[j],
		show=False)
		
	x1_plot.extend(x1_ext_plot)

x1_plot.title = 'Зависимость координаты материальной точки x от времени t'
x1_plot.xlabel = 't, с'
x1_plot.ylabel = 'x, м'
x1_plot.show()