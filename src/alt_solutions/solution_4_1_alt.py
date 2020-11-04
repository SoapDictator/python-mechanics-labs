import sympy as sym
import matplotlib.style as mplstl
import sympy.plotting as symplot

mplstl.use('seaborn-whitegrid')
line_colors = ['b', 'r', 'g', 'y', 't']

t = sym.Symbol('t')

a1 = 0.2
a2 = 0.3
om1 = 2

fi1 = sym.pi/4
fi2 = sym.pi/3

# 1
x = []
x.append(a1 * sym.sin(om1 * t + fi1))
x.append(a2 * sym.sin(om1 * t + fi2))
x.append(x[0] + x[1])

x_labels = ['x1', 'x2', 'x1+x2']

x_plot = sym.plot(legend=True, show=False)
for j in range(0, len(x)):
	x_ext_plot = sym.plot(
		x[j], (t, 0, 6),
		label=x_labels[j],
		line_color=line_colors[j],
		legend=True,
		show=False)
	x_plot.extend(x_ext_plot)
	
x_plot.title = 'Зависимость смещения маятника от времени'
x_plot.xlabel = 't, с'
x_plot.ylabel = 'x, м'
x_plot.show()